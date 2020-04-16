# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/listItem.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListItem(object):
    def setupUi(self, ListItem):
        ListItem.setObjectName("ListItem")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ListItem)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelItem = QtWidgets.QLabel(ListItem)
        self.labelItem.setBaseSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelItem.setFont(font)
        self.labelItem.setObjectName("labelItem")
        self.horizontalLayout.addWidget(self.labelItem)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.freshBar = QtWidgets.QProgressBar(ListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freshBar.sizePolicy().hasHeightForWidth())
        self.freshBar.setSizePolicy(sizePolicy)
        self.freshBar.setMaximumSize(QtCore.QSize(100, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.freshBar.setPalette(palette)
        self.freshBar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.freshBar.setProperty("value", 24)
        self.freshBar.setTextVisible(False)
        self.freshBar.setObjectName("freshBar")
        self.horizontalLayout.addWidget(self.freshBar)
        self.removeButton = QtWidgets.QPushButton(ListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setMaximumSize(QtCore.QSize(20, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.removeButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.removeButton.setFont(font)
        self.removeButton.setFlat(False)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout.addWidget(self.removeButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ListItem)
        QtCore.QMetaObject.connectSlotsByName(ListItem)

    def retranslateUi(self, ListItem):
        _translate = QtCore.QCoreApplication.translate
        self.labelItem.setText(_translate("ListItem", "TextLabel"))
        self.freshBar.setToolTip(_translate("ListItem", "freshness"))
        self.removeButton.setText(_translate("ListItem", "X"))
