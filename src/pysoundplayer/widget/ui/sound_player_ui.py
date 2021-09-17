# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sound_player.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from pyqtextra.common.jump_slider import JumpSlider

from . import sound_player_rc


class Ui_SoundPlayer(object):
    def setupUi(self, SoundPlayer):
        if not SoundPlayer.objectName():
            SoundPlayer.setObjectName(u"SoundPlayer")
        SoundPlayer.resize(870, 77)
        self.verticalLayout = QVBoxLayout(SoundPlayer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.slider_time = JumpSlider(SoundPlayer)
        self.slider_time.setObjectName(u"slider_time")
        self.slider_time.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slider_time)

        self.lbl_pos = QLabel(SoundPlayer)
        self.lbl_pos.setObjectName(u"lbl_pos")

        self.horizontalLayout.addWidget(self.lbl_pos)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_stop = QPushButton(SoundPlayer)
        self.btn_stop.setObjectName(u"btn_stop")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/stop", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stop.setIcon(icon)
        self.btn_stop.setIconSize(QSize(20, 20))
        self.btn_stop.setFlat(True)

        self.horizontalLayout_11.addWidget(self.btn_stop)

        self.btn_play = QPushButton(SoundPlayer)
        self.btn_play.setObjectName(u"btn_play")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_play.sizePolicy().hasHeightForWidth())
        self.btn_play.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/play", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/pause", QSize(), QIcon.Normal, QIcon.On)
        self.btn_play.setIcon(icon1)
        self.btn_play.setIconSize(QSize(20, 20))
        self.btn_play.setCheckable(True)
        self.btn_play.setFlat(True)

        self.horizontalLayout_11.addWidget(self.btn_play)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum
        )

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.label = QLabel(SoundPlayer)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label)

        self.cb_playbackSpeed = QComboBox(SoundPlayer)
        self.cb_playbackSpeed.setObjectName(u"cb_playbackSpeed")
        sizePolicy.setHeightForWidth(
            self.cb_playbackSpeed.sizePolicy().hasHeightForWidth()
        )
        self.cb_playbackSpeed.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.cb_playbackSpeed)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.retranslateUi(SoundPlayer)

        QMetaObject.connectSlotsByName(SoundPlayer)

    # setupUi

    def retranslateUi(self, SoundPlayer):
        SoundPlayer.setWindowTitle(
            QCoreApplication.translate("SoundPlayer", u"Form", None)
        )
        self.lbl_pos.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_stop.setToolTip(
            QCoreApplication.translate("SoundPlayer", u"Stop", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.btn_stop.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_play.setToolTip(
            QCoreApplication.translate("SoundPlayer", u"Play", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.btn_play.setText("")
        self.label.setText(
            QCoreApplication.translate("SoundPlayer", u"playback speed:", None)
        )

    # retranslateUi
