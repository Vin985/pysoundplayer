# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QSpectrogramViewer.ui'
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


class Ui_QSpectrogramViewer(object):
    def setupUi(self, QSpectrogramViewer):
        if QSpectrogramViewer.objectName():
            QSpectrogramViewer.setObjectName(u"QSpectrogramViewer")
        QSpectrogramViewer.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QSpectrogramViewer.sizePolicy().hasHeightForWidth())
        QSpectrogramViewer.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(QSpectrogramViewer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spectrogram_view = QGraphicsView(QSpectrogramViewer)
        self.spectrogram_view.setObjectName(u"spectrogram_view")

        self.horizontalLayout.addWidget(self.spectrogram_view)


        self.retranslateUi(QSpectrogramViewer)

        QMetaObject.connectSlotsByName(QSpectrogramViewer)
    # setupUi

    def retranslateUi(self, QSpectrogramViewer):
        QSpectrogramViewer.setWindowTitle(QCoreApplication.translate("QSpectrogramViewer", u"Form", None))
    # retranslateUi

