import random
import time

from PyQt6.QtGui import *
from PyQt6 import QtWidgets, QtGui, QtCore, uic
from PyQt6.QtWidgets import *
from math import log



class UIWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super(UIWidget, self).__init__()
        uic.loadUi("Taschenrechner.ui", self)

        #plus
        self.__btn_1 = self.findChild(QPushButton, "btn_1")
        self.__btn_1.clicked.connect(self.)
        #minus
        self.__btn_2 = self.findChild(QPushButton, "btn_1")
        self.__btn_2.clicked.connect(self.)
        # =
        self.__btn_3 = self.findChild(QPushButton, "btn_1")
        self.__btn_3.clicked.connect(self.)
        #9
        self.__btn_4 = self.findChild(QPushButton, "btn_1")
        self.__btn_4.clicked.connect(self.)
        #8
        self.__btn_5 = self.findChild(QPushButton, "btn_1")
        self.__btn_5.clicked.connect(self.)
        #7
        self.__btn_6 = self.findChild(QPushButton, "btn_1")
        self.__btn_6.clicked.connect(self.)
        #6
        self.__btn_7 = self.findChild(QPushButton, "btn_1")
        self.__btn_7.clicked.connect(self.)
        #5
        self.__btn_8 = self.findChild(QPushButton, "btn_1")
        self.__btn_8.clicked.connect(self.)
        #4
        self.__btn_9 = self.findChild(QPushButton, "btn_1")
        self.__btn_9.clicked.connect(self.)
        #3
        self.__btn_10 = self.findChild(QPushButton, "btn_1")
        self.__btn_10.clicked.connect(self.)
        #2
        self.__btn_11 = self.findChild(QPushButton, "btn_1")
        self.__btn_11.clicked.connect(self.)
        #1
        self.__btn_12 = self.findChild(QPushButton, "btn_1")
        self.__btn_12.clicked.connect(self.)
        #0
        self.__btn_13 = self.findChild(QPushButton, "btn_1")
        self.__btn_13.clicked.connect(self.)
        #clear
        self.__btn_14 = self.findChild(QPushButton, "btn_1")
        self.__btn_14.clicked.connect(self.)
        #*
        self.__btn_15 = self.findChild(QPushButton, "btn_1")
        self.__btn_15.clicked.connect(self.)
        #/
        self.__btn_16 = self.findChild(QPushButton, "btn_1")
        self.__btn_16.clicked.connect(self.)

        #lcd
        self.__lcd = self.findChild(QLCDNumber, "lcd")
        #self.__lcd.clicked.display(self.)

#display

    def eins(self):



    def sum(x, z, y):
      if z == "+":
        sum = x + y
      elif z == "-":
        sum = x - y
      elif z == "*":
        sum = x * y
      elif z == "/":
        sum = x / y
      else:
        return(sum)