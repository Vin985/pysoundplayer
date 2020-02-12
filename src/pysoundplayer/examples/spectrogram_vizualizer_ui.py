# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrogram_vizualizer.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from pysoundplayer.gui.QImageOptions import QImageOptions
from pysoundplayer.gui.QSpectrogramViewer import QSpectrogramViewer
from pysoundplayer.gui.QSpectrogramOptions import QSpectrogramOptions
from pysoundplayer.gui.QSoundPlayer import QSoundPlayer


class Ui_SpectrogramVizualizer(object):
    def setupUi(self, SpectrogramVizualizer):
        if SpectrogramVizualizer.objectName():
            SpectrogramVizualizer.setObjectName(u"SpectrogramVizualizer")
        SpectrogramVizualizer.resize(800, 600)
        self.centralwidget = QWidget(SpectrogramVizualizer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.spectrogram_viewer = QSpectrogramViewer(self.centralwidget)
        self.spectrogram_viewer.setObjectName(u"spectrogram_viewer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectrogram_viewer.sizePolicy().hasHeightForWidth())
        self.spectrogram_viewer.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.spectrogram_viewer)

        self.sound_player = QSoundPlayer(self.centralwidget)
        self.sound_player.setObjectName(u"sound_player")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sound_player.sizePolicy().hasHeightForWidth())
        self.sound_player.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.sound_player)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spectrogram_options = QSpectrogramOptions(self.groupBox)
        self.spectrogram_options.setObjectName(u"spectrogram_options")

        self.horizontalLayout_2.addWidget(self.spectrogram_options)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.image_options = QImageOptions(self.groupBox_2)
        self.image_options.setObjectName(u"image_options")

        self.horizontalLayout_3.addWidget(self.image_options)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        SpectrogramVizualizer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SpectrogramVizualizer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        SpectrogramVizualizer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SpectrogramVizualizer)
        self.statusbar.setObjectName(u"statusbar")
        SpectrogramVizualizer.setStatusBar(self.statusbar)

        self.retranslateUi(SpectrogramVizualizer)

        QMetaObject.connectSlotsByName(SpectrogramVizualizer)
    # setupUi

    def retranslateUi(self, SpectrogramVizualizer):
        SpectrogramVizualizer.setWindowTitle(QCoreApplication.translate("SpectrogramVizualizer", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("SpectrogramVizualizer", u"Spectrogram", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SpectrogramVizualizer", u"Image", None))
    # retranslateUi

