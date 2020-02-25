import pyaudio
from .audio import Audio


class SoundPlayer():
    def __init__(self):
        # init pyaudio
        self.pa = pyaudio.PyAudio()
        self.audio = None
        self.stream = None
        self.playing = False
        self.speed = 1
        self.done = False
        self.pos = 0

    def __del__(self):
        self.terminate()

    def open_stream(self):
        self.stream = self.pa.open(format=self.pa.get_format_from_width(self.audio.sample_width),
                                   channels=self.audio.nchannels,
                                   rate=int(self.audio.sr * self.speed),
                                   output=True,
                                   start=False,
                                   stream_callback=self.read_frames)

    def load(self, file_path):
        print("librosa loading: " + file_path)
        self.close_file()
        try:
            self.audio = Audio(file_path)
            self.open_stream()
            return self.audio
        except RuntimeError("Error, could not load file: " + file_path):
            return None

    def play(self):
        print("playing")
        if self.done:
            # File has already finished, restart stream
            print("resetting")
            self.stop()
            self.done = False
        self.playing = True
        self.stream.start_stream()

    def read_frames(self, input_data, frame_count, time_info, status):
        (data, new_pos, done) = self.audio.get_frames(
            self.pos, nframes=frame_count)
        # expected_size = self.audio.sample_width * frame_count * self.audio.nchannels
        # end_idx = self.pos + frame_count
        # data = []
        # if self.audio.nchannels == 1:
        #     data = self.audio[self.pos:end_idx]
        # else:
        #     data = self.audio[:, self.pos:end_idx]
        #     data = data.T.reshape((1, -1))
        self.pos = new_pos
        if done:
            self.done = True
            self.playing = False
        return (data, pyaudio.paContinue)

    def pause(self):
        if self.stream and self.stream.is_active():
            print("pausing")
            self.stream.stop_stream()
            self.playing = False

    def stop(self):
        if self.stream and self.audio is not None:
            print("stopping")
            self.playing = False
            self.stream.stop_stream()
            self.pos = 0
            # self.wave_file.rewind()

    def close_file(self):
        if self.stream:
            self.stream.close()

    def terminate(self):
        self.close_file()
        if self.pa:
            self.pa.terminate()

    def seek(self, pos):
        pos_frame = int(pos * self.audio.sr)
        self.pos = pos_frame

    def reset_stream(self):
        self.stream.close()
        self.open_stream()

    def change_speed(self, speed):
        self.speed = speed
        self.reset_stream()

    @property
    def duration(self):
        return self.audio.duration
