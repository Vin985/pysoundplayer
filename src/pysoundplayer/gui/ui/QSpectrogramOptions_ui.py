# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QSpectrogramOptions.ui'
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


class Ui_SpectrogramOptions(object):
    def setupUi(self, SpectrogramOptions):
        if SpectrogramOptions.objectName():
            SpectrogramOptions.setObjectName(u"SpectrogramOptions")
        SpectrogramOptions.resize(878, 283)
        self.horizontalLayout_2 = QHBoxLayout(SpectrogramOptions)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(SpectrogramOptions)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.cb_followSound = QCheckBox(self.groupBox)
        self.cb_followSound.setObjectName(u"cb_followSound")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_followSound.sizePolicy().hasHeightForWidth())
        self.cb_followSound.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.cb_followSound, 0, 0, 1, 3)

        self.cb_pcen = QCheckBox(self.groupBox)
        self.cb_pcen.setObjectName(u"cb_pcen")

        self.gridLayout_7.addWidget(self.cb_pcen, 1, 0, 1, 1)

        self.cb_remove_noise = QCheckBox(self.groupBox)
        self.cb_remove_noise.setObjectName(u"cb_remove_noise")

        self.gridLayout_7.addWidget(self.cb_remove_noise, 1, 3, 1, 1)

        self.cb_todb = QCheckBox(self.groupBox)
        self.cb_todb.setObjectName(u"cb_todb")

        self.gridLayout_7.addWidget(self.cb_todb, 1, 4, 1, 1)

        self.cb_normalize = QCheckBox(self.groupBox)
        self.cb_normalize.setObjectName(u"cb_normalize")

        self.gridLayout_7.addWidget(self.cb_normalize, 1, 5, 1, 1)

        self.label_40 = QLabel(self.groupBox)
        self.label_40.setObjectName(u"label_40")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.label_40, 2, 0, 1, 2)

        self.combo_fft = QComboBox(self.groupBox)
        self.combo_fft.setObjectName(u"combo_fft")

        self.gridLayout_7.addWidget(self.combo_fft, 2, 3, 1, 1)

        self.label_38 = QLabel(self.groupBox)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_7.addWidget(self.label_38, 2, 4, 1, 1)

        self.combo_window = QComboBox(self.groupBox)
        self.combo_window.setObjectName(u"combo_window")

        self.gridLayout_7.addWidget(self.combo_window, 2, 5, 1, 1)

        self.label_39 = QLabel(self.groupBox)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_7.addWidget(self.label_39, 3, 0, 1, 3)

        self.combo_hop_length = QComboBox(self.groupBox)
        self.combo_hop_length.setObjectName(u"combo_hop_length")

        self.gridLayout_7.addWidget(self.combo_hop_length, 3, 3, 1, 1)

        self.label_37 = QLabel(self.groupBox)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_7.addWidget(self.label_37, 3, 4, 1, 1)

        self.combo_scale = QComboBox(self.groupBox)
        self.combo_scale.setObjectName(u"combo_scale")

        self.gridLayout_7.addWidget(self.combo_scale, 3, 5, 1, 1)

        self.label_41 = QLabel(self.groupBox)
        self.label_41.setObjectName(u"label_41")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy2)
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_41, 4, 0, 1, 3)

        self.combo_specType = QComboBox(self.groupBox)
        self.combo_specType.addItem("")
        self.combo_specType.addItem("")
        self.combo_specType.setObjectName(u"combo_specType")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.combo_specType.sizePolicy().hasHeightForWidth())
        self.combo_specType.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.combo_specType, 4, 3, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(SpectrogramOptions)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_33 = QLabel(self.groupBox_2)
        self.label_33.setObjectName(u"label_33")
        sizePolicy1.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_33, 0, 0, 1, 2)

        self.label_35 = QLabel(self.groupBox_2)
        self.label_35.setObjectName(u"label_35")
        sizePolicy1.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy1)
        self.label_35.setWordWrap(True)

        self.gridLayout.addWidget(self.label_35, 2, 0, 1, 2)

        self.label_34 = QLabel(self.groupBox_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 3, 0, 1, 2)

        self.spin_height = QSpinBox(self.groupBox_2)
        self.spin_height.setObjectName(u"spin_height")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.spin_height.sizePolicy().hasHeightForWidth())
        self.spin_height.setSizePolicy(sizePolicy4)
        self.spin_height.setKeyboardTracking(False)
        self.spin_height.setMaximum(999)

        self.gridLayout.addWidget(self.spin_height, 3, 2, 1, 1)

        self.slider_contrast = QSlider(self.groupBox_2)
        self.slider_contrast.setObjectName(u"slider_contrast")
        sizePolicy4.setHeightForWidth(self.slider_contrast.sizePolicy().hasHeightForWidth())
        self.slider_contrast.setSizePolicy(sizePolicy4)
        self.slider_contrast.setMinimum(0)
        self.slider_contrast.setMaximum(5)
        self.slider_contrast.setSingleStep(5)
        self.slider_contrast.setTracking(False)
        self.slider_contrast.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_contrast, 1, 2, 1, 1)

        self.label_36 = QLabel(self.groupBox_2)
        self.label_36.setObjectName(u"label_36")
        sizePolicy1.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_36, 1, 0, 1, 1)

        self.spin_pix_in_sec = QSpinBox(self.groupBox_2)
        self.spin_pix_in_sec.setObjectName(u"spin_pix_in_sec")
        sizePolicy4.setHeightForWidth(self.spin_pix_in_sec.sizePolicy().hasHeightForWidth())
        self.spin_pix_in_sec.setSizePolicy(sizePolicy4)
        self.spin_pix_in_sec.setKeyboardTracking(False)
        self.spin_pix_in_sec.setMinimum(0)
        self.spin_pix_in_sec.setMaximum(999)

        self.gridLayout.addWidget(self.spin_pix_in_sec, 2, 2, 1, 1)

        self.cb_invert_colors = QCheckBox(self.groupBox_2)
        self.cb_invert_colors.setObjectName(u"cb_invert_colors")

        self.gridLayout.addWidget(self.cb_invert_colors, 4, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(378, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 0, 1, 3)

        self.combo_color_map = QComboBox(self.groupBox_2)
        self.combo_color_map.setObjectName(u"combo_color_map")
        sizePolicy4.setHeightForWidth(self.combo_color_map.sizePolicy().hasHeightForWidth())
        self.combo_color_map.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.combo_color_map, 0, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_2)


        self.retranslateUi(SpectrogramOptions)

        QMetaObject.connectSlotsByName(SpectrogramOptions)
    # setupUi

    def retranslateUi(self, SpectrogramOptions):
        SpectrogramOptions.setWindowTitle(QCoreApplication.translate("SpectrogramOptions", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("SpectrogramOptions", u"Spectrogram", None))
        self.cb_followSound.setText(QCoreApplication.translate("SpectrogramOptions", u"follow sound", None))
        self.cb_pcen.setText(QCoreApplication.translate("SpectrogramOptions", u"Use PCEN", None))
        self.cb_remove_noise.setText(QCoreApplication.translate("SpectrogramOptions", u"Remove noise", None))
        self.cb_todb.setText(QCoreApplication.translate("SpectrogramOptions", u"To dB", None))
        self.cb_normalize.setText(QCoreApplication.translate("SpectrogramOptions", u"Normalize", None))
        self.label_40.setText(QCoreApplication.translate("SpectrogramOptions", u"n_fft", None))
        self.label_38.setText(QCoreApplication.translate("SpectrogramOptions", u"Window type", None))
        self.label_39.setText(QCoreApplication.translate("SpectrogramOptions", u"hop length", None))
        self.label_37.setText(QCoreApplication.translate("SpectrogramOptions", u"Scale", None))
        self.label_41.setText(QCoreApplication.translate("SpectrogramOptions", u"spectrogram type:", None))
        self.combo_specType.setItemText(0, QCoreApplication.translate("SpectrogramOptions", u"audible range", None))
        self.combo_specType.setItemText(1, QCoreApplication.translate("SpectrogramOptions", u"ultra sonic range", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("SpectrogramOptions", u"Image", None))
        self.label_33.setText(QCoreApplication.translate("SpectrogramOptions", u"Color map", None))
        self.label_35.setText(QCoreApplication.translate("SpectrogramOptions", u"Number of pixels in a second", None))
        self.label_34.setText(QCoreApplication.translate("SpectrogramOptions", u"Height", None))
        self.label_36.setText(QCoreApplication.translate("SpectrogramOptions", u"Color contrast", None))
        self.cb_invert_colors.setText(QCoreApplication.translate("SpectrogramOptions", u"Invert colors", None))
    # retranslateUi

