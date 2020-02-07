from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow
from spectrogram_vizualizer_ui import Ui_SpectrogramVizualizer
from pysoundplayer.gui.settings import SoundPlayerSettings
import sys


class SpectrogramVizualizer(QMainWindow, Ui_SpectrogramVizualizer):
    def __init__(self):
        super(SpectrogramVizualizer, self).__init__()

        # Usual setup stuff. Set up the user interface from Designer
        self.setupUi(self)

        self.settings = SoundPlayerSettings()
        self.share_settings()

        audio = self.sound_player.load_file(
            file_path="/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/Priority/132133_SESA.wav")
        self.spectrogram_viewer.audio = audio

        self.link_events()
        self.show()

    def share_settings(self):
        self.spectrogram_viewer.settings = self.settings
        self.spectrogram_options.settings = self.settings

    def link_events(self):
        self.sound_player.update_position.connect(
            self.spectrogram_viewer.update_sound_marker)
        self.spectrogram_viewer.seek.connect(self.sound_player.seek)
        self.spectrogram_options.update_image.connect(
            self.spectrogram_viewer.update_image)
        self.spectrogram_options.update_spectrogram.connect(
            self.spectrogram_viewer.update_spectrogram)


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("ecosongs")
    app.setOrganizationDomain("https://github.com/vin985/pysoundplayer")
    app.setApplicationName("pysoundplayer")
    specviz = SpectrogramVizualizer()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
