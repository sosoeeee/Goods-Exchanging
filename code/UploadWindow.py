# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UploadWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Upload(object):
    def setupUi(self, Upload):
        Upload.setObjectName("Upload")
        Upload.resize(381, 303)
        self.layoutWidget = QtWidgets.QWidget(Upload)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 30, 262, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.label2 = QtWidgets.QLabel(self.layoutWidget)
        self.label2.setMinimumSize(QtCore.QSize(80, 0))
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 2, 0, 1, 1)
        self.want = QtWidgets.QLineEdit(self.layoutWidget)
        self.want.setObjectName("want")
        self.gridLayout.addWidget(self.want, 2, 1, 1, 1)
        self.label3 = QtWidgets.QLabel(self.layoutWidget)
        self.label3.setMinimumSize(QtCore.QSize(80, 0))
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 3, 0, 1, 1)
        self.info = QtWidgets.QLineEdit(self.layoutWidget)
        self.info.setObjectName("info")
        self.gridLayout.addWidget(self.info, 3, 1, 1, 1)
        self.hint = QtWidgets.QLabel(self.layoutWidget)
        self.hint.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hint.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hint.setObjectName("hint")
        self.gridLayout.addWidget(self.hint, 4, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.Confirm = QtWidgets.QPushButton(self.layoutWidget)
        self.Confirm.setStyleSheet("font: 12pt \"Adobe Heiti Std\";")
        self.Confirm.setObjectName("Confirm")
        self.gridLayout_2.addWidget(self.Confirm, 1, 0, 1, 1)
        self.Cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.Cancel.setStyleSheet("font: 12pt \"Adobe Heiti Std\";")
        self.Cancel.setObjectName("Cancel")
        self.gridLayout_2.addWidget(self.Cancel, 1, 1, 1, 1)

        self.retranslateUi(Upload)
        QtCore.QMetaObject.connectSlotsByName(Upload)

    def retranslateUi(self, Upload):
        _translate = QtCore.QCoreApplication.translate
        Upload.setWindowTitle(_translate("Upload", "Form"))
        self.label_5.setText(_translate("Upload", "种类："))
        self.label.setText(_translate("Upload", "物品："))
        self.label2.setText(_translate("Upload", "Wants："))
        self.label3.setText(_translate("Upload", "详细信息："))
        self.hint.setText(_translate("Upload", "[提示信息]"))
        self.Confirm.setText(_translate("Upload", "确定"))
        self.Cancel.setText(_translate("Upload", "取消"))

