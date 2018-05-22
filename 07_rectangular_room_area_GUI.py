#!/usr/bin/env python3

import sys
import math
from PyQt5 import QtCore, QtWidgets

CF = 0.09290304


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(330, 280)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget_1 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_1.setGeometry(QtCore.QRect(10, 20, 211, 80))
        self.gridLayoutWidget_1.setObjectName("gridLayoutWidget_1")

        self.gridLayout_1 = QtWidgets.QGridLayout(self.gridLayoutWidget_1)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setObjectName("gridLayout_1")

        self.length = QtWidgets.QLabel(self.gridLayoutWidget_1)
        self.length.setObjectName("length")
        self.gridLayout_1.addWidget(self.length, 0, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.lengthEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_1)
        self.lengthEdit.setObjectName("lengthEdit")
        self.gridLayout_1.addWidget(self.lengthEdit, 0, 1, 1, 1)

        self.width = QtWidgets.QLabel(self.gridLayoutWidget_1)
        self.width.setObjectName("width")
        self.gridLayout_1.addWidget(self.width, 1, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.widthEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_1)
        self.widthEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.widthEdit.setObjectName("widthEdit")
        self.gridLayout_1.addWidget(self.widthEdit, 1, 1, 1, 1)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(250, 20, 100, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.feetRadioButton = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.feetRadioButton.setChecked(True)
        self.feetRadioButton.setObjectName("feetRadioButton")
        self.gridLayout_2.addWidget(self.feetRadioButton, 0, 0, 1, 1)

        self.meterRadioButton = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.meterRadioButton.setObjectName("meterRadioButton")
        self.gridLayout_2.addWidget(self.meterRadioButton, 1, 0, 1, 1)

        self.Output = QtWidgets.QTextBrowser(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(15, 120, 300, 150))
        self.Output.setObjectName("Output")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Room Area"))
        self.length.setText(_translate("MainWindow", "Length"))
        self.width.setText(_translate("MainWindow", "Width"))
        self.feetRadioButton.setText(_translate("MainWindow", "Fee&t"))
        self.meterRadioButton.setText(_translate("MainWindow", "Meter"))

        self.lengthEdit.textChanged.connect(self.square_area)
        self.widthEdit.textChanged.connect(self.square_area)

        self.feetRadioButton.toggled.connect(self.square_area)
        self.meterRadioButton.toggled.connect(self.square_area)


    def square(self, var):
        return var ** 2

    def feet_to_meter(self, feet):
        return math.sqrt(self.square(feet) * CF)

    def meter_to_feet(self, meter):
        return math.sqrt(self.square(meter) / CF)

    def square_area(self):
        try:
            if self.lengthEdit.text() != '':
                length_f = float(self.lengthEdit.text())
                if self.widthEdit.text() != '':
                    width_f = float(self.widthEdit.text())
                    if self.feetRadioButton.isChecked():
                        self.Output.setText("The area is:\n"
                                            "{} square feet\n"
                                            "{} square meters".format((length_f * width_f),
                                                                      round(self.feet_to_meter(length_f) * self.feet_to_meter(width_f), 3)))
                    if self.meterRadioButton.isChecked():
                        self.Output.setText("The area is:\n"
                                            "{} square meters\n"
                                            "{} square feet".format((length_f * width_f),
                                                                    round(self.meter_to_feet(length_f) * self.meter_to_feet(width_f), 3)))
        except:
            self.Output.setText("Please enter numbers only.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
