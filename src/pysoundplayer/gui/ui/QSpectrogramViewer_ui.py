# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QSpectrogramViewer.ui',
# licensing of 'QSpectrogramViewer.ui' applies.
#
# Created: Fri Jan 31 16:13:22 2020
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SpectrogramViewer(object):
    def setupUi(self, SpectrogramViewer):
        SpectrogramViewer.setObjectName("SpectrogramViewer")
        SpectrogramViewer.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SpectrogramViewer.sizePolicy().hasHeightForWidth())
        SpectrogramViewer.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(SpectrogramViewer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spectrogram_view = QtWidgets.QGraphicsView(SpectrogramViewer)
        self.spectrogram_view.setObjectName("spectrogram_view")
        self.horizontalLayout.addWidget(self.spectrogram_view)

        self.retranslateUi(SpectrogramViewer)
        QtCore.QMetaObject.connectSlotsByName(SpectrogramViewer)

    def retranslateUi(self, SpectrogramViewer):
        SpectrogramViewer.setWindowTitle(QtWidgets.QApplication.translate("SpectrogramViewer", "Form", None, -1))

