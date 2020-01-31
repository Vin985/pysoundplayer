# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow
from pysoundplayer.gui.QSoundPlayer import QSoundPlayer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        # self.sound_player = QSoundPlayer(
        #     file_path="/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/Priority/132133_SESA.wav", parent=MainWindow)
        self.sound_player = QSoundPlayer(
            file_path="/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/Priority/54773_WRSA.wav", parent=MainWindow)
        self.sound_player.setObjectName("sound_player")
        # self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # self.gridLayoutWidget.setGeometry(QtCore.QRect(3, 1, 1114, 869))
        # self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        # self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        # self.gridLayout.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout.setObjectName("gridLayout")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
