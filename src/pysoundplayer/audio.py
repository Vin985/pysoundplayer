import librosa
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
        return self.data.__getitem__(index)

    def get_frames(self, pos, nframes):
        end_idx = pos + nframes
        data = []
        if self.nchannels == 1:
            data = self.data[pos:end_idx]
        else:
            data = self.data[:, pos:end_idx]
            data = data.T.reshape((1, -1))
        done = (end_idx >= self.nframes)
        return (data, end_idx, done)

    def get_spectrogram(self, options):
        if not self._spec:
            self._spec = Spectrogram(self, options)
        return self._spec

    def get_data(self, mono=True):
        if mono and self.nchannels == 2:
            return librosa.to_mono(self.data)
        return self.data
