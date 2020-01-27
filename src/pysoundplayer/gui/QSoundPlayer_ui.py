# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QSoundPlayer.ui',
# licensing of 'QSoundPlayer.ui' applies.
#
# Created: Fri Jan 24 15:50:51 2020
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from . import qsoundplayer_rc
from .QJumpSlider import QJumpSlider
from PySide2 import QtCore, QtGui, QtWidgets


class Ui_QSoundPlayer(object):
    def setupUi(self, QSoundPlayer):
        QSoundPlayer.setObjectName("QSoundPlayer")
        QSoundPlayer.resize(870, 70)
        self.verticalLayout = QtWidgets.QVBoxLayout(QSoundPlayer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slider_time = QJumpSlider(QSoundPlayer)
        self.slider_time.setOrientation(QtCore.Qt.Horizontal)
        self.slider_time.setObjectName("slider_time")
        self.horizontalLayout.addWidget(self.slider_time)
        self.lbl_pos = QtWidgets.QLabel(QSoundPlayer)
        self.lbl_pos.setText("")
        self.lbl_pos.setObjectName("lbl_pos")
        self.horizontalLayout.addWidget(self.lbl_pos)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_stop = QtWidgets.QPushButton(QSoundPlayer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy)
        self.btn_stop.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/stop"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon)
        self.btn_stop.setIconSize(QtCore.QSize(20, 20))
        self.btn_stop.setFlat(True)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_11.addWidget(self.btn_stop)
        self.btn_play = QtWidgets.QPushButton(QSoundPlayer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_play.sizePolicy().hasHeightForWidth())
        self.btn_play.setSizePolicy(sizePolicy)
        self.btn_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/play"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons/play"),
                        QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons/pause"),
                        QtGui.QIcon.Active, QtGui.QIcon.On)
        self.btn_play.setIcon(icon1)
        self.btn_play.setIconSize(QtCore.QSize(20, 20))
        self.btn_play.setCheckable(True)
        self.btn_play.setFlat(True)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout_11.addWidget(self.btn_play)
        self.btn_seek = QtWidgets.QPushButton(QSoundPlayer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_seek.sizePolicy().hasHeightForWidth())
        self.btn_seek.setSizePolicy(sizePolicy)
        self.btn_seek.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/signs"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_seek.setIcon(icon2)
        self.btn_seek.setIconSize(QtCore.QSize(20, 20))
        self.btn_seek.setFlat(True)
        self.btn_seek.setObjectName("btn_seek")
        self.horizontalLayout_11.addWidget(self.btn_seek)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.label = QtWidgets.QLabel(QSoundPlayer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignLeading |
                                QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        self.cb_playbackSpeed = QtWidgets.QComboBox(QSoundPlayer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cb_playbackSpeed.sizePolicy().hasHeightForWidth())
        self.cb_playbackSpeed.setSizePolicy(sizePolicy)
        self.cb_playbackSpeed.setObjectName("cb_playbackSpeed")
        self.horizontalLayout_11.addWidget(self.cb_playbackSpeed)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.retranslateUi(QSoundPlayer)
        QtCore.QMetaObject.connectSlotsByName(QSoundPlayer)

    def retranslateUi(self, QSoundPlayer):
        QSoundPlayer.setWindowTitle(
            QtWidgets.QApplication.translate("QSoundPlayer", "Form", None, -1))
        self.btn_stop.setToolTip(QtWidgets.QApplication.translate(
            "QSoundPlayer", "Stop", None, -1))
        self.btn_play.setToolTip(QtWidgets.QApplication.translate(
            "QSoundPlayer", "Play", None, -1))
        self.btn_seek.setToolTip(QtWidgets.QApplication.translate(
            "QSoundPlayer", "Seek", None, -1))
        self.label.setText(QtWidgets.QApplication.translate(
            "QSoundPlayer", "playback speed:", None, -1))
