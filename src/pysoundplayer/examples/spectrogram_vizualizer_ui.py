# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrogram_vizualizer.ui',
# licensing of 'spectrogram_vizualizer.ui' applies.
#
# Created: Thu Jan 30 12:46:39 2020
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SpectrogramVizualizer(object):
    def setupUi(self, SpectrogramVizualizer):
        SpectrogramVizualizer.setObjectName("SpectrogramVizualizer")
        SpectrogramVizualizer.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SpectrogramVizualizer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spectrogram_viewer = QSpectrogramViewer(self.centralwidget)
        self.spectrogram_viewer.setObjectName("spectrogram_viewer")
        self.verticalLayout.addWidget(self.spectrogram_viewer)
        self.sound_player = QSoundPlayer(self.centralwidget)
        self.sound_player.setObjectName("sound_player")
        self.verticalLayout.addWidget(self.sound_player)
        self.spectrogram_options = QSpectrogramOptions(self.centralwidget)
        self.spectrogram_options.setObjectName("spectrogram_options")
        self.verticalLayout.addWidget(self.spectrogram_options)
        SpectrogramVizualizer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SpectrogramVizualizer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        SpectrogramVizualizer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SpectrogramVizualizer)
        self.statusbar.setObjectName("statusbar")
        SpectrogramVizualizer.setStatusBar(self.statusbar)

        self.retranslateUi(SpectrogramVizualizer)
        QtCore.QMetaObject.connectSlotsByName(SpectrogramVizualizer)

    def retranslateUi(self, SpectrogramVizualizer):
        SpectrogramVizualizer.setWindowTitle(QtWidgets.QApplication.translate("SpectrogramVizualizer", "MainWindow", None, -1))

from pysoundplayer.gui.QSpectrogramViewer import QSpectrogramViewer
from pysoundplayer.gui.QSpectrogramOptions import QSpectrogramOptions
from pysoundplayer.gui.QSoundPlayer import QSoundPlayer
