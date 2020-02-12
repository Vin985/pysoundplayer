# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QSoundPlayer.ui'
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

from pysoundplayer.gui.QJumpSlider import QJumpSlider

from  . import qsoundplayer_rc

class Ui_QSoundPlayer(object):
    def setupUi(self, QSoundPlayer):
        if QSoundPlayer.objectName():
            QSoundPlayer.setObjectName(u"QSoundPlayer")
        QSoundPlayer.resize(870, 77)
        self.verticalLayout = QVBoxLayout(QSoundPlayer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.slider_time = QJumpSlider(QSoundPlayer)
        self.slider_time.setObjectName(u"slider_time")
        self.slider_time.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slider_time)

        self.lbl_pos = QLabel(QSoundPlayer)
        self.lbl_pos.setObjectName(u"lbl_pos")

        self.horizontalLayout.addWidget(self.lbl_pos)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_stop = QPushButton(QSoundPlayer)
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

        self.btn_play = QPushButton(QSoundPlayer)
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

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.label = QLabel(QSoundPlayer)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label)

        self.cb_playbackSpeed = QComboBox(QSoundPlayer)
        self.cb_playbackSpeed.setObjectName(u"cb_playbackSpeed")
        sizePolicy.setHeightForWidth(self.cb_playbackSpeed.sizePolicy().hasHeightForWidth())
        self.cb_playbackSpeed.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.cb_playbackSpeed)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_11)


        self.retranslateUi(QSoundPlayer)

        QMetaObject.connectSlotsByName(QSoundPlayer)
    # setupUi

    def retranslateUi(self, QSoundPlayer):
        QSoundPlayer.setWindowTitle(QCoreApplication.translate("QSoundPlayer", u"Form", None))
        self.lbl_pos.setText("")
#if QT_CONFIG(tooltip)
        self.btn_stop.setToolTip(QCoreApplication.translate("QSoundPlayer", u"Stop", None))
#endif // QT_CONFIG(tooltip)
        self.btn_stop.setText("")
#if QT_CONFIG(tooltip)
        self.btn_play.setToolTip(QCoreApplication.translate("QSoundPlayer", u"Play", None))
#endif // QT_CONFIG(tooltip)
        self.btn_play.setText("")
        self.label.setText(QCoreApplication.translate("QSoundPlayer", u"playback speed:", None))
    # retranslateUi

