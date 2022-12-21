from PySide6 import QtCore, QtWidgets, QtGui

import datetime as dt

from ..sound_player import SoundPlayer
from .ui.sound_player_ui import Ui_SoundPlayer


class SoundPlayerWidget(QtWidgets.QWidget, Ui_SoundPlayer):

    SOUNDS_SPEEDS = [0.1, 0.125, 0.2, 0.25, 0.5, 1, 2]

    TOOLTIP_PLAY = "Play"
    TOOLTIP_PAUSE = "Pause"
    SLIDER_INTERVAL = 0.1  # seconds
    UPDATE_REFRESH_INTERVAL = 100  # miliseconds

    update_position = QtCore.Signal(float)
    start_playing = QtCore.Signal()

    def __init__(self, parent=None, file_path=None):
        super().__init__(parent)
        self.setupUi(self)
        self.file_path = file_path
        self.sound_player = SoundPlayer()
        self.audio = None
        self.position = 0.0
        self.last_update = None
        self.playing = False
        self.update_timer = QtCore.QTimer()
        self.sound_speed = 1
        self.link_events()
        self.define_shortcuts()
        self.init_playback_speeds()
        if self.file_path is not None:
            self.load_file()

    def audio_loaded(self):
        return self.audio is not None

    @property
    def sr(self):
        return self.audio.sr

    @property
    def duration(self):
        return self.audio.duration

    def link_events(self):
        self.btn_play.clicked.connect(self.play_pause)
        self.btn_stop.clicked.connect(self.stop)
        self.cb_playbackSpeed.activated.connect(self.change_playback_speed)
        self.update_timer.timeout.connect(self.update_sound_position)
        self.slider_time.seek_position.connect(self.seek_slider)

    def define_shortcuts(self):
        QtGui.QShortcut(
            QtGui.QKeySequence(QtCore.Qt.Key_Space), self, self.btn_play.click
        )

    def init_playback_speeds(self):
        self.cb_playbackSpeed.clear()
        self.cb_playbackSpeed.insertItems(0, [str(x) for x in self.SOUNDS_SPEEDS])
        self.cb_playbackSpeed.setCurrentIndex(
            self.SOUNDS_SPEEDS.index(self.sound_speed)
        )

    def load_file(self, file_path=None):
        if file_path is not None:
            self.file_path = file_path
        if self.file_path is None:
            print("Error, no file path found, please provide one")
            return
        self.audio = self.sound_player.load(self.file_path)
        self.slider_time.setMaximum(self.duration / self.SLIDER_INTERVAL)
        self.update_position_label()
        return self.audio

    def play_pause(self):
        if self.playing:
            self.pause()
        else:
            self.play()

    def play(self):
        self.start_playing.emit()
        self.playing = True
        if self.sound_player.done:
            self.position = 0
        self.update_play_btn(self.TOOLTIP_PAUSE)
        self.sound_player.play()
        self.last_update = dt.datetime.now()
        self.update_timer.start(100)

    def pause(self):
        self.playing = False
        self.sound_player.pause()
        self.update_play_btn(self.TOOLTIP_PLAY)
        self.update_timer.stop()

    def stop(self):
        self.playing = False
        self.sound_player.stop()
        self.update_timer.stop()
        self.position = 0
        self.update_position_ui()
        self.update_play_btn(self.TOOLTIP_PLAY, checked=False)

    def seek(self, pos, from_slider=False):
        self.position = pos
        self.sound_player.seek(pos)
        if from_slider:
            # Seek has been done using the slider. Do not update the slider
            self.update_position_ui(slider=False)
        else:
            # Update everything
            self.update_sound_position()

    def seek_slider(self, value):
        self.seek(value * self.SLIDER_INTERVAL, from_slider=True)

    def change_playback_speed(self, idx):
        speed = float(self.cb_playbackSpeed.itemText(idx))
        self.sound_speed = speed
        self.sound_player.change_speed(self.sound_speed)

    def terminate(self):
        self.sound_player.terminate()

    ###################
    ### GUI UPDATES ###
    ###################

    def update_sound_position(self):

        # TODO: Use sound player information instead!
        if self.playing:
            currentTime = dt.datetime.now()
            increment = (currentTime - self.last_update).total_seconds()
            self.position += increment * self.sound_speed
            self.last_update = currentTime
            if self.position > self.duration:  # self.sound_player.done:
                self.position = self.duration
                self.btn_play.click()
        self.update_position_ui()

    def update_position_ui(self, slider=True):
        self.update_position_label()
        if slider:
            self.update_slider()
        self.update_position.emit(self.position)

    def update_slider(self):
        slider_pos = int(self.position / self.SLIDER_INTERVAL)
        self.slider_time.setSliderPosition(slider_pos)

    def update_position_label(self):
        pos = str(round(self.position, 2))
        dur = str(round(self.duration, 2))
        self.lbl_pos.setText("/".join([pos, dur]))

    def update_play_btn(self, tooltip="", checked=None):
        self.btn_play.setToolTip(tooltip)
        if checked is not None:
            self.btn_play.setChecked(checked)
