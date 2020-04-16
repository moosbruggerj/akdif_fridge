#!/usr/bin/env python3
import sys

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QLabel, QListWidgetItem, QWidget
from PyQt5.QtCore import QDate, QTimer
from PyQt5.QtGui import QColor, QPalette

import ui.listItem as listItem
import ui.mainWindow as mainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.items = []
        self.isOpen = False
        self.now = QDate.currentDate()

        datestr = self.now.toString("dd.MM.yyyy")
        self.ui.dateLabel.setText(f"Date: {datestr}")

        self.timer_days = QTimer(self)
        self.timer_days.start(2000)
        self.timer_days.timeout.connect(self.nextDay)

        self.ui.insertButton.clicked.connect(self.insertItem)
        self.ui.openButton.clicked.connect(self.toggleOpen)
    
    def removeItem(self, item):
        row = self.ui.listWidget.row(item.listWidget)
        self.ui.listWidget.takeItem(row)
        self.items.remove(item)
        
    def nextDay(self):
        self.now = self.now.addDays(1)
        for item in self.items:
            item.setStatus(self.now)
            
        datestr = self.now.toString("dd.MM.yyyy")
        self.ui.dateLabel.setText(f"Date: {datestr}")

    def toggleOpen(self):
        self.isOpen = not self.isOpen
        self.ui.insertButton.setEnabled(self.isOpen)

        for item in self.items:
            item.setEnabled(self.isOpen)

        if self.isOpen:
            self.ui.openButton.setText("Close Fridge")
        else:
            self.ui.openButton.setText("Open Fridge")

    def insertItem(self):
        name = self.ui.itemNameEdit.text()
        if name == "":
            self.ui.statusbar.showMessage("Item must have a name", 2000)
            return
        item = ListItem(self, name, self.now, self.ui.dateEdit.date())
        self.ui.listWidget.setItemWidget(item.listWidget, item.widget)
        self.items.append(item)
        pass


class ListItem:
    def __init__(self, window, name, now, freshUntil):
        self.window = window
        self.listWidget = QListWidgetItem(window.ui.listWidget)
        self.widget = QWidget(self.window)
        self.ui = listItem.Ui_ListItem()
        self.ui.setupUi(self.widget)
        self.ui.labelItem.setText(name)
        self.insert = now
        self.freshUntil = freshUntil
        self.name = name
        self.expired = False

        self.currentCategory = 0

        self.thresholds = [(100, QColor(0x55, 0xff, 0x7f)), (50, QColor(0xff, 0xaa, 0x00)), (25, QColor(0xff, 0x55, 0x00))]

        self.ui.removeButton.clicked.connect(self.removeClicked)
        self.setStatus(now)

    def setStatus(self, now:QDate):
        if self.expired:
            return

        remaining = now.daysTo(self.freshUntil)
        if remaining < 0:
            self.expired = True
            color = QColor(0xff, 0x9b, 0x9b)
            palette = self.widget.palette()
            palette.setColor(self.widget.backgroundRole(), color)
            self.widget.setPalette(palette)
            self.listWidget.setBackground(color)
            return

        fraction = int(float(remaining) / self.insert.daysTo(self.freshUntil) * 100)
        category = self.currentCategory
        for i in range(len(self.thresholds)):
            if fraction < self.thresholds[i][0]:
                category = i

        if category != self.currentCategory:
            self.currentCategory = category
            palette = self.ui.freshBar.palette()
            palette.setColor(QPalette.Highlight, self.thresholds[category][1])
            self.ui.freshBar.setPalette(palette)

        self.ui.freshBar.setValue(fraction)

    def setEnabled(self, enabled):
        self.ui.removeButton.setEnabled(enabled)


    def removeClicked(self):
        self.window.removeItem(self)



class test:
    def __init__(self):
        self.test2 = test2()

    def modify(self):
        self.test2.data = "modified data"

class test2(test):
    def __init__(self):
        self.data = "test data"


#t = test()
#data = t.test2
#print(f"data: {data.data}")
#t.modify()
#print(f"data after mod: {data.data}")

#exit(0)

app = QApplication(sys.argv)
win = MainWindow()


win.show()
sys.exit(app.exec_())
