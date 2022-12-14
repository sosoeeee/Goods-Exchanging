# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Console(object):
    def setupUi(self, Console):
        Console.setObjectName("Console")
        Console.resize(579, 620)
        self.label = QtWidgets.QLabel(Console)
        self.label.setGeometry(QtCore.QRect(40, 20, 101, 41))
        self.label.setStyleSheet("font: 11pt \"黑体\";")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Console)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 101, 41))
        self.label_2.setStyleSheet("font: 11pt \"黑体\";")
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.manageDone = QtWidgets.QPushButton(Console)
        self.manageDone.setGeometry(QtCore.QRect(40, 540, 491, 51))
        self.manageDone.setStyleSheet("font: 11pt \"Adobe Heiti Std\";")
        self.manageDone.setObjectName("manageDone")
        self.widget = QtWidgets.QWidget(Console)
        self.widget.setGeometry(QtCore.QRect(40, 300, 491, 218))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("font: 10pt \"宋体\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("font: 10pt \"宋体\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)
        self.passedUsers = QtWidgets.QListWidget(self.widget)
        self.passedUsers.setObjectName("passedUsers")
        self.gridLayout_4.addWidget(self.passedUsers, 1, 1, 1, 1)
        self.notPassUsers = QtWidgets.QListWidget(self.widget)
        self.notPassUsers.setObjectName("notPassUsers")
        self.gridLayout_4.addWidget(self.notPassUsers, 1, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(Console)
        self.widget1.setGeometry(QtCore.QRect(41, 81, 491, 151))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.sortsBox = QtWidgets.QComboBox(self.widget1)
        self.sortsBox.setObjectName("sortsBox")
        self.gridLayout.addWidget(self.sortsBox, 0, 1, 1, 1)
        self.addSort = QtWidgets.QPushButton(self.widget1)
        self.addSort.setObjectName("addSort")
        self.gridLayout.addWidget(self.addSort, 0, 2, 1, 1)
        self.delSort = QtWidgets.QPushButton(self.widget1)
        self.delSort.setObjectName("delSort")
        self.gridLayout.addWidget(self.delSort, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setStyleSheet("font: 11pt \"黑体\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.sortName = QtWidgets.QLineEdit(self.widget1)
        self.sortName.setObjectName("sortName")
        self.gridLayout_3.addWidget(self.sortName, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setStyleSheet("font: 11pt \"黑体\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.sortInfo = QtWidgets.QLineEdit(self.widget1)
        self.sortInfo.setObjectName("sortInfo")
        self.gridLayout_3.addWidget(self.sortInfo, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.hint = QtWidgets.QLabel(self.widget1)
        self.hint.setObjectName("hint")
        self.gridLayout_2.addWidget(self.hint, 2, 0, 1, 1)

        self.retranslateUi(Console)
        QtCore.QMetaObject.connectSlotsByName(Console)

    def retranslateUi(self, Console):
        _translate = QtCore.QCoreApplication.translate
        Console.setWindowTitle(_translate("Console", "Form"))
        self.label.setText(_translate("Console", "类别管理"))
        self.label_2.setText(_translate("Console", "用户审核"))
        self.manageDone.setText(_translate("Console", "完成"))
        self.label_3.setText(_translate("Console", "审核未通过"))
        self.label_4.setText(_translate("Console", "审核已通过"))
        self.label_7.setText(_translate("Console", "           "))
        self.addSort.setText(_translate("Console", "+"))
        self.delSort.setText(_translate("Console", "-"))
        self.label_5.setText(_translate("Console", "名称："))
        self.label_6.setText(_translate("Console", "详细信息："))
        self.hint.setText(_translate("Console", "[提示信息]"))
