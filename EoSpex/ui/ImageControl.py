# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/fisher/Dropbox/PycharmProjects/EOVSASpex/EoSpex/ui/ImageControl.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageControl(object):
    def setupUi(self, ImageControl):
        ImageControl.setObjectName("ImageControl")
        ImageControl.resize(293, 661)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(ImageControl)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_dataField = QtWidgets.QGroupBox(ImageControl)
        self.groupBox_dataField.setMaximumSize(QtCore.QSize(16777215, 51))
        self.groupBox_dataField.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_dataField.setObjectName("groupBox_dataField")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_dataField)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.control_dataField = QtWidgets.QComboBox(self.groupBox_dataField)
        self.control_dataField.setObjectName("control_dataField")
        self.verticalLayout_3.addWidget(self.control_dataField)
        self.verticalLayout_5.addWidget(self.groupBox_dataField)
        self.groupBox_displayMode = QtWidgets.QGroupBox(ImageControl)
        self.groupBox_displayMode.setMaximumSize(QtCore.QSize(16777215, 51))
        self.groupBox_displayMode.setFocusPolicy(QtCore.Qt.TabFocus)
        self.groupBox_displayMode.setObjectName("groupBox_displayMode")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_displayMode)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.control_displayMode = QtWidgets.QComboBox(self.groupBox_displayMode)
        self.control_displayMode.setObjectName("control_displayMode")
        self.horizontalLayout.addWidget(self.control_displayMode)
        self.verticalLayout_5.addWidget(self.groupBox_displayMode)
        self.slicer_group = QtWidgets.QGroupBox(ImageControl)
        self.slicer_group.setMinimumSize(QtCore.QSize(0, 250))
        self.slicer_group.setObjectName("slicer_group")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.slicer_group)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(17, 198, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.slicer_group)
        self.control_DataRange_GBox = QtWidgets.QGroupBox(ImageControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_DataRange_GBox.sizePolicy().hasHeightForWidth())
        self.control_DataRange_GBox.setSizePolicy(sizePolicy)
        self.control_DataRange_GBox.setMinimumSize(QtCore.QSize(0, 0))
        self.control_DataRange_GBox.setMaximumSize(QtCore.QSize(16777215, 115))
        self.control_DataRange_GBox.setObjectName("control_DataRange_GBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.control_DataRange_GBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Slider_dmax_GBox = QtWidgets.QGroupBox(self.control_DataRange_GBox)
        self.Slider_dmax_GBox.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Slider_dmax_GBox.setFont(font)
        self.Slider_dmax_GBox.setObjectName("Slider_dmax_GBox")
        self.gridLayout = QtWidgets.QGridLayout(self.Slider_dmax_GBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Slider_dmax = QtWidgets.QSlider(self.Slider_dmax_GBox)
        self.Slider_dmax.setMaximumSize(QtCore.QSize(16777215, 22))
        self.Slider_dmax.setMaximum(99)
        self.Slider_dmax.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_dmax.setObjectName("Slider_dmax")
        self.gridLayout.addWidget(self.Slider_dmax, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.Slider_dmax_GBox)
        self.Slider_dmin_GBox = QtWidgets.QGroupBox(self.control_DataRange_GBox)
        self.Slider_dmin_GBox.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Slider_dmin_GBox.setFont(font)
        self.Slider_dmin_GBox.setObjectName("Slider_dmin_GBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Slider_dmin_GBox)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Slider_dmin = QtWidgets.QSlider(self.Slider_dmin_GBox)
        self.Slider_dmin.setMaximumSize(QtCore.QSize(16777215, 22))
        self.Slider_dmin.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_dmin.setObjectName("Slider_dmin")
        self.gridLayout_3.addWidget(self.Slider_dmin, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.Slider_dmin_GBox)
        self.verticalLayout_5.addWidget(self.control_DataRange_GBox)
        self.control_imageOperations_Gbox = QtWidgets.QGroupBox(ImageControl)
        self.control_imageOperations_Gbox.setMinimumSize(QtCore.QSize(250, 0))
        self.control_imageOperations_Gbox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.control_imageOperations_Gbox.setObjectName("control_imageOperations_Gbox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.control_imageOperations_Gbox)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.control_colorBar_check = QtWidgets.QCheckBox(self.control_imageOperations_Gbox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.control_colorBar_check.setFont(font)
        self.control_colorBar_check.setChecked(True)
        self.control_colorBar_check.setObjectName("control_colorBar_check")
        self.gridLayout_2.addWidget(self.control_colorBar_check, 2, 0, 1, 1)
        self.control_colorNorm_check = QtWidgets.QCheckBox(self.control_imageOperations_Gbox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.control_colorNorm_check.setFont(font)
        self.control_colorNorm_check.setChecked(False)
        self.control_colorNorm_check.setObjectName("control_colorNorm_check")
        self.gridLayout_2.addWidget(self.control_colorNorm_check, 1, 0, 1, 2)
        self.control_abs_check = QtWidgets.QCheckBox(self.control_imageOperations_Gbox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.control_abs_check.setFont(font)
        self.control_abs_check.setObjectName("control_abs_check")
        self.gridLayout_2.addWidget(self.control_abs_check, 1, 2, 1, 1)
        self.rotate_dial = QtWidgets.QDial(self.control_imageOperations_Gbox)
        self.rotate_dial.setMaximum(3)
        self.rotate_dial.setPageStep(1)
        self.rotate_dial.setSliderPosition(0)
        self.rotate_dial.setTracking(True)
        self.rotate_dial.setOrientation(QtCore.Qt.Horizontal)
        self.rotate_dial.setNotchesVisible(True)
        self.rotate_dial.setObjectName("rotate_dial")
        self.gridLayout_2.addWidget(self.rotate_dial, 1, 3, 2, 1)
        self.control_log_check = QtWidgets.QCheckBox(self.control_imageOperations_Gbox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.control_log_check.setFont(font)
        self.control_log_check.setObjectName("control_log_check")
        self.gridLayout_2.addWidget(self.control_log_check, 2, 1, 1, 2)
        self.verticalLayout_5.addWidget(self.control_imageOperations_Gbox)
        self.Slider_alpha_GBox = QtWidgets.QGroupBox(ImageControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_alpha_GBox.sizePolicy().hasHeightForWidth())
        self.Slider_alpha_GBox.setSizePolicy(sizePolicy)
        self.Slider_alpha_GBox.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Slider_alpha_GBox.setFont(font)
        self.Slider_alpha_GBox.setObjectName("Slider_alpha_GBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Slider_alpha_GBox)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Slider_alpha = QtWidgets.QSlider(self.Slider_alpha_GBox)
        self.Slider_alpha.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Slider_alpha.setFont(font)
        self.Slider_alpha.setMaximum(100)
        self.Slider_alpha.setProperty("value", 100)
        self.Slider_alpha.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_alpha.setObjectName("Slider_alpha")
        self.gridLayout_5.addWidget(self.Slider_alpha, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.Slider_alpha_GBox)
        self.control_colorSelector_GBox = QtWidgets.QGroupBox(ImageControl)
        self.control_colorSelector_GBox.setMaximumSize(QtCore.QSize(16777215, 77))
        self.control_colorSelector_GBox.setObjectName("control_colorSelector_GBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.control_colorSelector_GBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.control_colors_list = QtWidgets.QComboBox(self.control_colorSelector_GBox)
        self.control_colors_list.setObjectName("control_colors_list")
        self.verticalLayout.addWidget(self.control_colors_list)
        self.verticalLayout_5.addWidget(self.control_colorSelector_GBox)
        self.groupBox_dataField.raise_()
        self.slicer_group.raise_()
        self.control_DataRange_GBox.raise_()
        self.control_imageOperations_Gbox.raise_()
        self.groupBox_displayMode.raise_()
        self.Slider_alpha_GBox.raise_()
        self.control_colorSelector_GBox.raise_()

        self.retranslateUi(ImageControl)
        QtCore.QMetaObject.connectSlotsByName(ImageControl)

    def retranslateUi(self, ImageControl):
        _translate = QtCore.QCoreApplication.translate
        ImageControl.setWindowTitle(_translate("ImageControl", "Form"))
        self.groupBox_dataField.setTitle(_translate("ImageControl", "Data Field"))
        self.groupBox_displayMode.setTitle(_translate("ImageControl", "Display Mode"))
        self.slicer_group.setTitle(_translate("ImageControl", "Data Slicer"))
        self.control_DataRange_GBox.setTitle(_translate("ImageControl", "Data Range"))
        self.Slider_dmax_GBox.setTitle(_translate("ImageControl", "dmax"))
        self.Slider_dmin_GBox.setTitle(_translate("ImageControl", "dmin"))
        self.control_imageOperations_Gbox.setTitle(_translate("ImageControl", "Image Operations"))
        self.control_colorBar_check.setText(_translate("ImageControl", "Color Bar"))
        self.control_colorNorm_check.setText(_translate("ImageControl", "Color Normalize"))
        self.control_abs_check.setText(_translate("ImageControl", "ABS"))
        self.control_log_check.setText(_translate("ImageControl", "LOG"))
        self.Slider_alpha_GBox.setTitle(_translate("ImageControl", "Image alpha"))
        self.control_colorSelector_GBox.setTitle(_translate("ImageControl", "Color Selector"))

