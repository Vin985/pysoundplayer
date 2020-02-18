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

        self.spectrogram_vizualizer.load_file(
            "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/Priority/132133_SESA.wav")
        self.show()


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("ecosongs")
    app.setOrganizationDomain("https://github.com/vin985/pysoundplayer")
    app.setApplicationName("pysoundplayer")
    specviz = SpectrogramVizualizer()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
