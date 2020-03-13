import librosa
import soundfile
from .spectrogram.spectrogram import Spectrogram


class Audio():
    def __init__(self, file_path, sr=None, mono=False, **kwargs):
        self.file_path = file_path
        (self.data, self.sr) = (librosa.load(
            file_path, sr=sr, mono=mono, **kwargs))
        self.nchannels = len(self.data.shape)
        self.nframes = self.data.shape[self.nchannels - 1]
        self.duration = self.nframes / self.sr
        self.sample_width = self.data.dtype.itemsize
        self._spec = None

    def __getitem__(self, index):
        if self.nchannels == 1:
            data = self.data[index]
        else:
            data = self.data[:, index]
        return data

    def get_frames(self, start, end=None, nframes=None):
        if not end and not nframes:
            raise AttributeError(
                "Either the attribute 'end' with the position of ending frame or 'nframes' with the number of frames desired is required")
        end_idx = end or start + nframes
        data = []
        data = self[start:end_idx]
        if self.nchannels > 1:
            data = data.T.reshape((1, -1))
        done = (end_idx >= self.nframes)
        return (data, end_idx, done)

    def get_spectrogram(self, options, recreate=False):
        if not self._spec or recreate:
            self._spec = Spectrogram(self, options)
        return self._spec

    def get_data(self, mono=True):
        if mono and self.nchannels == 2:
            return librosa.to_mono(self.data)
        return self.data

    def frames_to_seconds(self, frames):
        return frames / self.sr

    def get_silences(self, *args, min_dur=1, **kwargs):
        res = []
        if self.data is not None and self.data.size:
            sound_intervals = librosa.effects.split(self.data, *args, **kwargs)
            start = 0
            end = 0
            for interval in sound_intervals:
                if (interval[1] - interval[0]) < (min_dur * self.sr * self.nchannels):
                    continue
                end = interval[0]
                if end > start:
                    res.append((start, end))
                start = interval[1]

            # Special case where the file ends with a silence
            if start < self.nframes:
                end = self.nframes
                res.append((start, end))

        return res

    def get_sound_intervals(self, *args, min_sound_duration=1, min_silence_duration=1, **kwargs):
        res = []
        if self.data is not None and self.data.size:
            sound_intervals = librosa.effects.split(self.data, *args, **kwargs)
            start = 0
            end = 0
            last_silence_start = 0
            last_silence_end = 0
            last_sound = []
            for interval in sound_intervals:

                last_silence_end = interval[0]

                duration = self.frames_to_seconds(interval[1] - interval[0])
                # if the sounds lasts less than minimum duration, consider it a silence
                if duration < min_sound_duration:
                    last_silence_end = interval[1]
                    continue

                # File starts with a silence
                if start == 0 and interval[0] > 0:
                    # Keep the silence if it lasts less than minimum duration
                    if self.frames_to_seconds(interval[0]) > min_silence_duration:
                        start = interval[0]
                else:
                    start = interval[0]

                # The last silence was shorter than the minimum duration: keep it as sound
                if last_silence_end > 0 and (last_silence_end - last_silence_start) < min_silence_duration:
                    last_sound[1] = interval[1]
                    last_silence_start = interval[1]
                    continue

                end = interval[1]
                last_silence_start = interval[1]
                last_sound = [start, end]
                res.append(last_sound)
        return res

    def write(self, file_path, start=None, end=None):
        if start is None and end is None:
            data = self.data
        else:
            if start is not None and end is not None:
                data = self[start:end]
            else:
                raise AttributeError(
                    "Both start and end arguments should be provided")

        if self.nchannels > 1:
            data = data.T

        soundfile.write(file_path, data, samplerate=self.sr)
