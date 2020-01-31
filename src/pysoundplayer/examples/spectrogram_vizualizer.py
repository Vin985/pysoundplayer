from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow
from .spectrogram_vizualizer_ui import Ui_SpectrogramVizualizer
import sys


class SpectrogramVizualizer(QMainWindow, Ui_SpectrogramVizualizer):
    def __init__(self):
        super(SpectrogramVizualizer, self).__init__()

        # Usual setup stuff. Set up the user interface from Designer
        self.setupUi(self)

        audio = self.sound_player.load_file(
            file_path="/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/Priority/132133_SESA.wav")
        self.spectrogram_viewer.audio = audio
        self.show()


def main():
    app = QApplication(sys.argv)
    specviz = SpectrogramVizualizer()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
