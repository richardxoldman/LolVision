# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
from check_values import check_values
from check_values_to_save import check_values_to_save
from get_data_from_gui import get_data_from_gui
from generate_graphs import Worker


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.119091, y1:0.188, x2:1, y2:1, stop:0 rgba(0, 89, 167, 255), stop:1 rgba(140, 174, 200, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 1021, 91))
        self.label.setStyleSheet("font: 50pt \"Arial\";\n"
"color: rgb(255, 255, 255)\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 580, 371, 81))
        self.pushButton.setStyleSheet("border-radius:15px;\n"
"border: 4px solid black;\n"
"background-color: rgb(209, 122, 0);\n"
"font: 30pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1060, 350, 200, 60))
        self.pushButton_2.setStyleSheet("border-radius:15px;\n"
"border: 3px solid black;\n"
"background-color: rgb(88, 189, 44);\n"
"font: 24pt \"Arial\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(60, 520, 351, 51))
        # self.checkBox.setSizeIncrement(QtCore.QSize(0, 0))
        # self.checkBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox::indicator {width: 20px; height: 20px;}")
        # self.checkBox.setIconSize(QtCore.QSize(100, 100))
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 440, 401, 41))
        self.label_2.setStyleSheet("font: 20pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 480, 231, 31))
        self.label_3.setStyleSheet("font: 14pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 440, 101, 41))
        self.lineEdit.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 200, 91, 41))
        self.label_4.setStyleSheet("font: 20pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 200, 91, 41))
        self.lineEdit_2.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 200, 91, 41))
        self.lineEdit_3.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 200, 91, 41))
        self.label_5.setStyleSheet("font: 20pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(720, 200, 91, 41))
        self.label_6.setStyleSheet("font: 20pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(820, 200, 91, 41))
        self.lineEdit_4.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1030, 200, 91, 41))
        self.label_7.setStyleSheet("font: 20pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(1120, 200, 91, 41))
        self.lineEdit_5.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 280, 91, 41))
        self.label_8.setStyleSheet("font: 20pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 280, 81, 41))
        self.lineEdit_6.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(710, 280, 111, 41))
        self.label_9.setStyleSheet("font: 20pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(470, 280, 91, 41))
        self.lineEdit_7.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(820, 280, 91, 41))
        self.lineEdit_8.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 280, 91, 41))
        self.label_10.setStyleSheet("font: 20pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(1120, 280, 91, 41))
        self.lineEdit_9.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1020, 280, 101, 41))
        self.label_11.setStyleSheet("font: 20pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 360, 351, 41))
        self.label_12.setStyleSheet("font: 20pt \"Arial\";")
        self.label_12.setObjectName("label_12")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(370, 360, 61, 41))
        self.lineEdit_10.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(450, 360, 61, 41))
        self.lineEdit_11.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(530, 360, 61, 41))
        self.lineEdit_12.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(280, 109, 351, 41))
        self.label_13.setStyleSheet("font: 20pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(570, 110, 401, 41))
        self.comboBox.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(590, 440, 401, 41))
        self.label_14.setStyleSheet("font: 20pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(740, 440, 281, 41))
        self.lineEdit_13.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(790, 362, 260, 41))
        self.lineEdit_14.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(1110, 441, 101, 41))
        self.comboBox_2.setStyleSheet("border: 3px solid black;\n"
"font: 20pt \"Arial\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1050, 440, 61, 41))
        self.label_15.setStyleSheet("font: 20pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 27))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(568, 540, 401, 41))
        self.label_16.setStyleSheet("font: 20pt \"Arial\";")
        self.label_16.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(624, 360, 170, 41))
        self.label_17.setStyleSheet("font: 20pt \"Arial\";")
        self.label_17.setObjectName("label_17")

        with open("leagues.json") as data_file:
            self.leagues_data = json.load(data_file)
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.pushButton.clicked.connect(self.check_and_run_generator)
        self.pushButton_2.clicked.connect(self.check_and_save_data)

        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LoLVision"))
        self.label.setText(_translate("MainWindow", "League of Legends Vision Graphs"))
        self.pushButton.setText(_translate("MainWindow", "Generate Graphs"))
        self.pushButton_2.setText(_translate("MainWindow", "Save Data"))
        self.checkBox.setText(_translate("MainWindow", "Generate with map legend"))
        self.label_2.setText(_translate("MainWindow", "Detection confidence threshold"))
        self.label_3.setText(_translate("MainWindow", "(suggested value ~0.75)"))
        self.label_4.setText(_translate("MainWindow", "Map X"))
        self.label_5.setText(_translate("MainWindow", "Map Y"))
        self.label_6.setText(_translate("MainWindow", "Map W"))
        self.label_7.setText(_translate("MainWindow", "Map H"))
        self.label_8.setText(_translate("MainWindow", "Timer Y"))
        self.label_9.setText(_translate("MainWindow", "Timer W"))
        self.label_10.setText(_translate("MainWindow", "Timer X"))
        self.label_11.setText(_translate("MainWindow", "Timer H"))
        self.label_12.setText(_translate("MainWindow", "Widths between timer digits"))
        self.label_13.setText(_translate("MainWindow", "Load data from league"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Custom"))
        self.label_14.setText(_translate("MainWindow", "Team name"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "blue"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "red"))
        self.label_15.setText(_translate("MainWindow", "Side"))
        self.label_17.setText(_translate("MainWindow", "Save data as"))

    def report_progress(self, n):
        self.label_16.setText(f"Step: {n}/3")

    def load_data_from_leagues(self):
        for league in self.leagues_data["leagues"]:
            self.comboBox.addItem(league["name"])

    def on_combobox_changed(self):
        if self.comboBox.currentText() == "Custom":
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.lineEdit_8.setText("")
            self.lineEdit_9.setText("")
            self.lineEdit_10.setText("")
            self.lineEdit_11.setText("")
            self.lineEdit_12.setText("")
            return True

        for row in self.leagues_data["leagues"]:
            if row["name"] == self.comboBox.currentText():
                self.lineEdit_2.setText(str(row["map_data"]["map_x"]))
                self.lineEdit_3.setText(str(row["map_data"]["map_y"]))
                self.lineEdit_4.setText(str(row["map_data"]["map_w"]))
                self.lineEdit_5.setText(str(row["map_data"]["map_h"]))
                self.lineEdit_6.setText(str(row["timer_data"]["timer_x"]))
                self.lineEdit_7.setText(str(row["timer_data"]["timer_y"]))
                self.lineEdit_8.setText(str(row["timer_data"]["timer_w"]))
                self.lineEdit_9.setText(str(row["timer_data"]["timer_h"]))
                self.lineEdit_10.setText(str(row["widths_between_digits"]["first"]))
                self.lineEdit_11.setText(str(row["widths_between_digits"]["second"]))
                self.lineEdit_12.setText(str(row["widths_between_digits"]["third"]))

    def show_value_error(self, text):
        message = QtWidgets.QMessageBox()
        message.setWindowTitle("Error")
        message.setText(text)
        message.setIcon(QtWidgets.QMessageBox.Warning)

        x = message.exec_()

    def check_and_run_generator(self):
        if check_values(self) is True:
            data = get_data_from_gui(self)
            self.thread = QtCore.QThread()
            self.worker = Worker(data)
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.generate_graphs)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.progress.connect(self.report_progress)

            self.thread.start()
            self.pushButton.setEnabled(False)
            self.thread.finished.connect(lambda: self.pushButton.setEnabled(True))
            self.thread.finished.connect(lambda: self.label_16.setText(""))

    def check_and_save_data(self):
        if check_values_to_save(self) is True:
            new_league_data = {
                "name": self.lineEdit_14.text(),
                "timer_data": {
                    "timer_x": int(self.lineEdit_6.text()),
                    "timer_y": int(self.lineEdit_7.text()),
                    "timer_w": int(self.lineEdit_8.text()),
                    "timer_h": int(self.lineEdit_9.text())
                },
                "map_data": {
                    "map_x": int(self.lineEdit_2.text()),
                    "map_y": int(self.lineEdit_3.text()),
                    "map_w": int(self.lineEdit_4.text()),
                    "map_h": int(self.lineEdit_5.text())
                },
                "widths_between_digits":{
                    "first": int(self.lineEdit_10.text()),
                    "second": int(self.lineEdit_11.text()),
                    "third": int(self.lineEdit_12.text())
                }
            }
            self.leagues_data["leagues"].append(new_league_data)

            with open("leagues.json", "w") as data_file:
                json.dump(self.leagues_data, data_file)
            self.comboBox.addItem(self.lineEdit_14.text())
            self.pushButton_2.setText("Data Saved")
            self.pushButton_2.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.load_data_from_leagues()

    MainWindow.show()
    sys.exit(app.exec_())

