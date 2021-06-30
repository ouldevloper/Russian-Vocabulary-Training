# -*- coding: utf-8 -*-

from os import error, times
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import random
import time
import sys
import datetime
from verb import verb
from verb import User
from verb import Settings
from verb import lang
from word import Word
from word import Word_trans

import os
sys.path.append(os.path.realpath('.'))

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(552, 552)
                MainWindow.setMinimumSize(QtCore.QSize(552, 552))
                MainWindow.setMaximumSize(QtCore.QSize(552, 552))
                MainWindow.setStyleSheet("color:white;\n"
                                        "background-color: rgb(61, 56, 70);\n"
                                        "margin:0px;\n"
                                        "padding:0px;")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
                self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 534, 534))
                self.stackedWidget.setMinimumSize(QtCore.QSize(534, 534))
                self.stackedWidget.setStyleSheet("color: rgb(255, 255, 255);")
                self.stackedWidget.setObjectName("stackedWidget")
                self.page = QtWidgets.QWidget()
                self.page.setObjectName("page")
                self.answer_word = QtWidgets.QLineEdit(self.page)
                self.answer_word.setGeometry(QtCore.QRect(0, 500, 481, 27))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.answer_word.sizePolicy().hasHeightForWidth())
                self.answer_word.setSizePolicy(sizePolicy)
                self.answer_word.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.answer_word.setStyleSheet("background-color: rgb(154, 153, 150);\n"
                                                "border-radius:5px;\n"
                                                "margin-left:10px;")
                self.answer_word.setObjectName("answer_word")
                self.skip_word = QtWidgets.QPushButton(self.page)
                self.skip_word.setGeometry(QtCore.QRect(510, 20, 21, 21))
                self.skip_word.setStyleSheet("border-radius:10px;\n"
                                                        "font: 16pt \"Cantarell\";\n"
                                                        "background-color: rgb(245, 194, 17);\n"
                                                        "\n"
                                                        "")
                self.skip_word.setObjectName("skip_word")
                self.layoutWidget_12 = QtWidgets.QWidget(self.page)
                self.layoutWidget_12.setGeometry(QtCore.QRect(0, 0, 381, 21))
                self.layoutWidget_12.setObjectName("layoutWidget_12")
                self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget_12)
                self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_13.setObjectName("horizontalLayout_13")
                self.info_word = QtWidgets.QLabel(self.layoutWidget_12)
                self.info_word.setObjectName("info_word")
                self.horizontalLayout_13.addWidget(self.info_word)
                self.help_foreign_word = QtWidgets.QPushButton(self.page)
                self.help_foreign_word.setGeometry(QtCore.QRect(510, 380, 21, 21))
                self.help_foreign_word.setStyleSheet("border-radius:10px;\n"
                                                        "font: 16pt \"Cantarell\";\n"
                                                        "background-color: rgb(98, 160, 234);\n"
                                                        "\n"
                                                        "")
                self.help_foreign_word.setObjectName("help_foreign_word") 
                self.clear_word = QtWidgets.QPushButton(self.page)
                self.clear_word.setGeometry(QtCore.QRect(470, 500, 51, 27))
                self.clear_word.setMaximumSize(QtCore.QSize(70, 100))
                self.clear_word.setStyleSheet("background-color: rgb(46, 194, 126);\n"
                                                "border-radius:10px;\n"
                                                "color:white;\n"
                                                "border-radius:10px;")
                self.clear_word.setObjectName("clear_word")
                self.help_native_word = QtWidgets.QPushButton(self.page)
                self.help_native_word.setGeometry(QtCore.QRect(510, 260, 21, 21))
                self.help_native_word.setStyleSheet("border-radius:10px;\n"
                                                        "font: 16pt \"Cantarell\";\n"
                                                        "background-color: rgb(98, 160, 234);\n"
                                                        "\n"
                                                        "")
                self.help_native_word.setObjectName("help_native_word")
                self.layoutWidget_13 = QtWidgets.QWidget(self.page)
                self.layoutWidget_13.setGeometry(QtCore.QRect(0, 20, 531, 471))
                self.layoutWidget_13.setObjectName("layoutWidget_13")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_13)
                self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.gridLayout_4 = QtWidgets.QGridLayout()
                self.gridLayout_4.setObjectName("gridLayout_4")
                self.new_lang_word = QtWidgets.QLabel(self.layoutWidget_13)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.new_lang_word.setFont(font)
                self.new_lang_word.setStyleSheet("margin:10px;\n"
                                                "background-color: rgb(153, 193, 241);\n"
                                                "border-radius: 10px;")
                self.new_lang_word.setText("")
                self.new_lang_word.setAlignment(QtCore.Qt.AlignCenter)
                self.new_lang_word.setObjectName("new_lang_word")
                self.gridLayout_4.addWidget(self.new_lang_word, 0, 0, 1, 1)
                self.verticalLayout_3.addLayout(self.gridLayout_4)
                self.native_lang_word = QtWidgets.QLabel(self.layoutWidget_13)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.native_lang_word.setFont(font)
                self.native_lang_word.setStyleSheet("background-color: rgb(249, 240, 107);\n"
                                                                "margin:10px;\n"
                                                                "border-radius:10px;")
                self.native_lang_word.setText("")
                self.native_lang_word.setAlignment(QtCore.Qt.AlignCenter)
                self.native_lang_word.setObjectName("native_lang_verb_word")
                self.verticalLayout_3.addWidget(self.native_lang_word)
                self.new_lang_extra_word = QtWidgets.QLabel(self.layoutWidget_13)
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.new_lang_extra_word.setFont(font)
                self.new_lang_extra_word.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.new_lang_extra_word.setStyleSheet("background-color: rgb(255, 163, 72);\n"
                                                        "border-radius:10px;\n"
                                                        "margin:10px;")
                self.new_lang_extra_word.setText("")
                self.new_lang_extra_word.setAlignment(QtCore.Qt.AlignCenter)
                self.new_lang_extra_word.setObjectName("new_lang_extra_word")
                self.verticalLayout_3.addWidget(self.new_lang_extra_word)
                self.native_lang_extra_word = QtWidgets.QLabel(self.layoutWidget_13)
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.native_lang_extra_word.setFont(font)
                self.native_lang_extra_word.setStyleSheet("background-color: rgb(246, 97, 81);\n"
                                                                "border-radius:10px;\n"
                                                                "margin:10px;")
                self.native_lang_extra_word.setText("")
                self.native_lang_extra_word.setAlignment(QtCore.Qt.AlignCenter)
                self.native_lang_extra_word.setObjectName("native_lang_extra_word")
                self.verticalLayout_3.addWidget(self.native_lang_extra_word)
                self.new_lang_extra_word.raise_()
                self.native_lang_word.raise_()
                self.native_lang_extra_word.raise_()
                self.answer_word.raise_()
                self.layoutWidget_12.raise_()
                self.clear_word.raise_()
                self.layoutWidget_13.raise_()
                self.skip_word.raise_()
                self.help_foreign_word.raise_()
                self.help_native_word.raise_()
                self.stackedWidget.addWidget(self.page)
                self.stackedWidgetPage1 = QtWidgets.QWidget()
                self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
                self.layoutWidget = QtWidgets.QWidget(self.stackedWidgetPage1)
                self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 531, 471))
                self.layoutWidget.setObjectName("layoutWidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.gridLayout_2 = QtWidgets.QGridLayout()
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.new_lang = QtWidgets.QLabel(self.layoutWidget)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.new_lang.setFont(font)
                self.new_lang.setStyleSheet("margin:10px;\n"
                                                "background-color: rgb(153, 193, 241);\n"
                                                "border-radius: 10px;")
                self.new_lang.setText("")
                self.new_lang.setAlignment(QtCore.Qt.AlignCenter)
                self.new_lang.setObjectName("new_lang")
                self.gridLayout_2.addWidget(self.new_lang, 0, 0, 1, 1)
                self.verticalLayout.addLayout(self.gridLayout_2)
                self.new_lang_extra = QtWidgets.QLabel(self.layoutWidget)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.new_lang_extra.setFont(font)
                self.new_lang_extra.setStyleSheet("background-color: rgb(249, 240, 107);\n"
                                                        "margin:10px;\n"
                                                        "border-radius:10px;")
                self.new_lang_extra.setText("")
                self.new_lang_extra.setAlignment(QtCore.Qt.AlignCenter)
                self.new_lang_extra.setObjectName("new_lang_extra")
                self.verticalLayout.addWidget(self.new_lang_extra)
                self.native_lang_verb = QtWidgets.QLabel(self.layoutWidget)
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.native_lang_verb.setFont(font)
                self.native_lang_verb.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.native_lang_verb.setStyleSheet("background-color: rgb(255, 163, 72);\n"
                                                        "border-radius:10px;\n"
                                                        "margin:10px;")
                self.native_lang_verb.setText("")
                self.native_lang_verb.setAlignment(QtCore.Qt.AlignCenter)
                self.native_lang_verb.setObjectName("native_lang_verb")
                self.verticalLayout.addWidget(self.native_lang_verb)
                self.foreing_lang_verb = QtWidgets.QLabel(self.layoutWidget)
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.foreing_lang_verb.setFont(font)
                self.foreing_lang_verb.setStyleSheet("background-color: rgb(246, 97, 81);\n"
                                                        "border-radius:10px;\n"
                                                        "margin:10px;")
                self.foreing_lang_verb.setText("")
                self.foreing_lang_verb.setAlignment(QtCore.Qt.AlignCenter)
                self.foreing_lang_verb.setObjectName("foreing_lang_verb")
                self.verticalLayout.addWidget(self.foreing_lang_verb)
                self.help_native = QtWidgets.QPushButton(self.stackedWidgetPage1)
                self.help_native.setGeometry(QtCore.QRect(510, 260, 21, 21))
                self.help_native.setStyleSheet("border-radius:10px;\n"
                                                        "font: 16pt \"Cantarell\";\n"
                                                        "background-color: rgb(98, 160, 234);\n"
                                                        "\n"
                                                        "")
                self.help_native.setObjectName("help_native")
                self.clear = QtWidgets.QPushButton(self.stackedWidgetPage1)
                self.clear.setGeometry(QtCore.QRect(470, 500, 51, 27))
                self.clear.setMaximumSize(QtCore.QSize(70, 100))
                self.clear.setStyleSheet("background-color: rgb(46, 194, 126);\n"
                                                "border-radius:10px;\n"
                                                "color:white;\n"
                                                "border-radius:10px;")
                self.clear.setObjectName("clear")
                self.skip = QtWidgets.QPushButton(self.stackedWidgetPage1)
                self.skip.setGeometry(QtCore.QRect(510, 20, 21, 21))
                self.skip.setStyleSheet("border-radius:10px;\n"
                                        "font: 16pt \"Cantarell\";\n"
                                        "background-color: rgb(245, 194, 17);\n"
                                        "\n"
                                        "")
                self.skip.setObjectName("skip")
                self.answer = QtWidgets.QLineEdit(self.stackedWidgetPage1)
                self.answer.setGeometry(QtCore.QRect(0, 500, 481, 27))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.answer.sizePolicy().hasHeightForWidth())
                self.answer.setSizePolicy(sizePolicy)
                self.answer.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.answer.setStyleSheet("background-color: rgb(154, 153, 150);\n"
                                                "border-radius:5px;\n"
                                                "margin-left:10px;")
                self.answer.setObjectName("answer")
                self.help_foreign = QtWidgets.QPushButton(self.stackedWidgetPage1)
                self.help_foreign.setGeometry(QtCore.QRect(510, 380, 21, 21))
                self.help_foreign.setStyleSheet("border-radius:10px;\n"
                                                "font: 16pt \"Cantarell\";\n"
                                                "background-color: rgb(98, 160, 234);\n"
                                                "\n"
                                                "")
                self.help_foreign.setObjectName("help_foreign")
                self.layoutWidget1 = QtWidgets.QWidget(self.stackedWidgetPage1)
                self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 381, 21))
                self.layoutWidget1.setObjectName("layoutWidget1")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.info = QtWidgets.QLabel(self.layoutWidget1)
                self.info.setObjectName("info")
                self.horizontalLayout_2.addWidget(self.info)
                self.stackedWidget.addWidget(self.stackedWidgetPage1)
                self.stackedWidgetPage2 = QtWidgets.QWidget()
                self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
                self.groupBox_2 = QtWidgets.QGroupBox(self.stackedWidgetPage2)
                self.groupBox_2.setGeometry(QtCore.QRect(9, 50, 521, 211))
                self.groupBox_2.setObjectName("groupBox_2")
                self.layoutWidget_5 = QtWidgets.QWidget(self.groupBox_2)
                self.layoutWidget_5.setGeometry(QtCore.QRect(130, 100, 331, 43))
                self.layoutWidget_5.setObjectName("layoutWidget_5")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
                self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.label_5 = QtWidgets.QLabel(self.layoutWidget_5)
                self.label_5.setObjectName("label_5")
                self.horizontalLayout_5.addWidget(self.label_5)
                self.foreign_lang = QtWidgets.QComboBox(self.layoutWidget_5)
                self.foreign_lang.setStyleSheet("QComboBox{\n"
                                                "border:                 none;\n"
                                                "background-color:   rgb(87, 96, 134);\n"
                                                "color:                      rgb(255, 255, 255);\n"
                                                "font-weight:            bold;\n"
                                                "padding:                    5px; \n"
                                                "border-radius:0px;\n"
                                                "}\n"
                                                "\n"
                                                "QComboBox::drop-down{\n"
                                                "    border:                 none;\n"
                                                "    background-color:   rgb(87, 96, 134);\n"
                                                "    color:                     black;\n"
                                                "    font-weight:            bold;\n"
                                                "    padding:                    10px;\n"
                                                "}\n"
                                                "\n"
                                                "QComboBox::down-arrow{ \n"
                                                "   padding-right:          5px;\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "")
                self.foreign_lang.setIconSize(QtCore.QSize(0, 0))
                self.foreign_lang.setObjectName("foreign_lang")
                self.foreign_lang.addItem("")
                self.foreign_lang.addItem("")
                self.foreign_lang.addItem("")
                self.foreign_lang.addItem("")
                self.horizontalLayout_5.addWidget(self.foreign_lang)
                self.layoutWidget_6 = QtWidgets.QWidget(self.groupBox_2)
                self.layoutWidget_6.setGeometry(QtCore.QRect(130, 50, 331, 53))
                self.layoutWidget_6.setObjectName("layoutWidget_6")
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
                self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.label_6 = QtWidgets.QLabel(self.layoutWidget_6)
                self.label_6.setObjectName("label_6")
                self.horizontalLayout_6.addWidget(self.label_6)
                self.native_lang = QtWidgets.QComboBox(self.layoutWidget_6)
                self.native_lang.setStyleSheet("QComboBox{\n"
                                                "border:                 none;\n"
                                                "background-color:   rgb(87, 96, 134);\n"
                                                "color:                      rgb(255, 255, 255);\n"
                                                "font-weight:            bold;\n"
                                                "padding:                    5px; \n"
                                                "border-radius:0px;\n"
                                                "margin:0px;\n"
                                                "}\n"
                                                "\n"
                                                "QComboBox::drop-down{\n"
                                                "    border:                 none;\n"
                                                "    background-color:   rgb(87, 96, 134);\n"
                                                "    color:                     black;\n"
                                                "    font-weight:            bold;\n"
                                                "    padding:                    10px;\n"
                                                "}\n"
                                                "\n"
                                                "QComboBox::down-arrow{ \n"
                                                "   padding-right:          5px;\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "")
                self.native_lang.setIconSize(QtCore.QSize(0, 0))
                self.native_lang.setObjectName("native_lang")
                self.native_lang.addItem("")
                self.native_lang.addItem("")
                self.native_lang.addItem("")
                self.native_lang.addItem("")
                self.horizontalLayout_6.addWidget(self.native_lang)
                self.save_lang = QtWidgets.QPushButton(self.groupBox_2)
                self.save_lang.setGeometry(QtCore.QRect(350, 150, 111, 27))
                self.save_lang.setStyleSheet("background-color:#007fff;")
                self.save_lang.setObjectName("save_lang")
                self.groupBox = QtWidgets.QGroupBox(self.stackedWidgetPage2)
                self.groupBox.setGeometry(QtCore.QRect(9, 270, 521, 191))
                self.groupBox.setStyleSheet("border-bottom-color: rgb(255, 255, 255);")
                self.groupBox.setObjectName("groupBox")
                self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox)
                self.layoutWidget_3.setGeometry(QtCore.QRect(130, 90, 331, 41))
                self.layoutWidget_3.setObjectName("layoutWidget_3")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
                self.label_3.setObjectName("label_3")
                self.horizontalLayout_3.addWidget(self.label_3)
                self.words_run = QtWidgets.QSpinBox(self.layoutWidget_3)
                self.words_run.setMaximumSize(QtCore.QSize(16777215, 30))
                self.words_run.setStyleSheet("background-color:   rgb(87, 96, 134);\n"
                                                "color:                      rgb(255, 255, 255);\n"
                                                "border-radius:0px;\n"
                                                "margin:0x;\n"
                                                "padding:0px;")
                self.words_run.setObjectName("words_run")
                self.horizontalLayout_3.addWidget(self.words_run)
                self.layoutWidget_4 = QtWidgets.QWidget(self.groupBox)
                self.layoutWidget_4.setGeometry(QtCore.QRect(130, 40, 331, 41))
                self.layoutWidget_4.setObjectName("layoutWidget_4")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
                self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.label_4 = QtWidgets.QLabel(self.layoutWidget_4)
                self.label_4.setObjectName("label_4")
                self.horizontalLayout_4.addWidget(self.label_4)
                self.nickname = QtWidgets.QLineEdit(self.layoutWidget_4)
                self.nickname.setMaximumSize(QtCore.QSize(16777215, 30))
                self.nickname.setStyleSheet("background-color:   rgb(87, 96, 134);\n"
                                                "color:                      rgb(255, 255, 255);\n"
                                                "border-radius:0px;\n"
                                                "margin:0x;\n"
                                                "padding:0px;")
                self.nickname.setObjectName("nickname")
                self.horizontalLayout_4.addWidget(self.nickname)
                self.save_user = QtWidgets.QPushButton(self.groupBox)
                self.save_user.setGeometry(QtCore.QRect(350, 140, 111, 27))
                self.save_user.setStyleSheet("background-color:#007fff;")
                self.save_user.setObjectName("save_user")
                self.groupBox_3 = QtWidgets.QGroupBox(self.stackedWidgetPage2)
                self.groupBox_3.setGeometry(QtCore.QRect(9, 533, 527, 50))
                self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 50))
                self.groupBox_3.setTitle("")
                self.groupBox_3.setObjectName("groupBox_3")
                self.stackedWidget.addWidget(self.stackedWidgetPage2)
                self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
                self.layoutWidget2.setGeometry(QtCore.QRect(470, -1, 71, 31))
                self.layoutWidget2.setObjectName("layoutWidget2")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.back = QtWidgets.QPushButton(self.layoutWidget2)
                self.back.setStyleSheet("QPushButto{\n"
                                        "color:white;\n"
                                        "background-color: rgb(61, 56, 70);\n"
                                        "margin:0px;\n"
                                        "padding:0px;\n"
                                        "border:none;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButto:pressed{\n"
                                        "color:white;\n"
                                        "background-color: rgb(61, 56, 70);\n"
                                        "margin:0px;\n"
                                        "padding:0px;\n"
                                        "}\n"
                                        "QPushButto:hover{\n"
                                        "color:white;\n"
                                        "background-color: rgb(61, 56, 70);\n"
                                        "margin:0px;\n"
                                        "padding:0px;\n"
                                        "}")
                self.back.setObjectName("back")
                self.horizontalLayout.addWidget(self.back)
                self.next = QtWidgets.QPushButton(self.layoutWidget2)
                self.next.setStyleSheet("QPushButto{\n"
                                        "color:white;\n"
                                        "background-color: rgb(61, 56, 70);\n"
                                        "margin:0px;\n"
                                        "padding:0px;\n"
                                        "border:none;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButto:pressed{\n"
                                        "color:white;\n"
                                        "background-color: rgb(61, 56, 70);\n"
                                        "margin:0px;\n"
                                        "padding:0px;\n"
                                        "}\n"
                                        "QPushButto:hover{\n"
                                        "color:white;\n"
                                        "background-color: rgb(61, 56, 70);\n"
                                        "margin:0px;\n"
                                        "padding:0px;\n"
                                        "}")
                self.next.setObjectName("next")
                self.horizontalLayout.addWidget(self.next)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.stackedWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "500 Comman Russian Verbs"))
                self.skip_word.setText(_translate("MainWindow", "x"))
                self.info_word.setText(_translate("MainWindow", "UNKNOW | Level 1"))
                self.help_foreign_word.setText(_translate("MainWindow", "?"))
                self.clear_word.setText(_translate("MainWindow", "  C"))
                self.help_native_word.setText(_translate("MainWindow", "?"))
                self.help_native.setText(_translate("MainWindow", "?"))
                self.clear.setText(_translate("MainWindow", "  C"))
                self.skip.setText(_translate("MainWindow", "x"))
                self.help_foreign.setText(_translate("MainWindow", "?"))
                self.info.setText(_translate("MainWindow", "UNKNOW | Level 1"))
                self.groupBox_2.setTitle(_translate("MainWindow", "Language Settings"))
                self.label_5.setText(_translate("MainWindow", "  Native Lnaguage"))
                self.foreign_lang.setItemText(0, _translate("MainWindow", "en"))
                self.foreign_lang.setItemText(1, _translate("MainWindow", "ar"))
                self.foreign_lang.setItemText(2, _translate("MainWindow", "fr"))
                self.foreign_lang.setItemText(3, _translate("MainWindow", "ru"))
                self.label_6.setText(_translate("MainWindow", "  Native Lnaguage"))
                self.native_lang.setItemText(0, _translate("MainWindow", "en"))
                self.native_lang.setItemText(1, _translate("MainWindow", "ar"))
                self.native_lang.setItemText(2, _translate("MainWindow", "fr"))
                self.native_lang.setItemText(3, _translate("MainWindow", "ru"))
                self.save_lang.setText(_translate("MainWindow", "Save"))
                self.groupBox.setTitle(_translate("MainWindow", "User Settings"))
                self.label_3.setText(_translate("MainWindow", "  words/run"))
                self.label_4.setText(_translate("MainWindow", "  Nick name"))
                self.save_user.setText(_translate("MainWindow", "Save"))
                self.back.setText(_translate("MainWindow", "<<"))
                self.next.setText(_translate("MainWindow", ">>"))


                self.word_answers    = []
                self.answers    = []
                self.word       = None
                self.verb       = None
                self.native     = None
                self.foreing    = None
                self.user       = None
                self.word_count = None

                self.next.clicked.connect(self.next_clicked)
                self.back.clicked.connect(self.back_clicked)
                self.clear.clicked.connect(self.clear_clicked)
                self.save_lang.clicked.connect(self.save_lang_clicked)
                self.save_user.clicked.connect(self.save_user_clicked)
                self.skip.clicked.connect(self.skipclicked)
                self.help_native.clicked.connect(self.help_native_clicked)
                self.help_foreign.clicked.connect(self.help_foreign_clicked)
                self.answer.returnPressed.connect(self.clicked_submit)

                self.clear_word.clicked.connect(self.clear_word_clicked)
                self.skip_word.clicked.connect(self.skip_word_clicked)
                self.help_native_word.clicked.connect(self.help_native_word_clicked)
                self.help_foreign_word.clicked.connect(self.help_foreign_word_clicked)
                self.answer_word.returnPressed.connect(self.answer_word_pressed)
                
                
                self.init_settings()
                self.init()
                self.init_word()
                
                
                
        def next_clicked(self):
                if self.stackedWidget.currentIndex() in [0,1]:
                        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()+1)
                else:
                        self.stackedWidget.setCurrentIndex(0)
        def back_clicked(self):
                if self.stackedWidget.currentIndex() in [1,2]:
                        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()-1)
                else:
                        self.stackedWidget.setCurrentIndex(2)
        def init_settings(self):
                user = User()
                sett = Settings()
                self.native     = sett.native_lang
                self.foreing    = sett.foreing_lang
                self.user       = user.user
                self.word_count = user.word_count
                self.native_lang.setCurrentText(sett.native_lang)
                self.foreign_lang.setCurrentText(sett.foreing_lang)
                self.nickname.setText(user.user)
                self.words_run.setValue(int(user.word_count))
        def save_user_clicked(self):
                user = User(self.nickname.text(),self.words_run.value()) 
                self.user = user.user
                self.word_count = user.word_count 
                user.update()     
        def save_lang_clicked(self):
                sett = Settings(1,self.native_lang.currentText(),self.foreign_lang.currentText())
                self.native = sett.native_lang
                self.foreing = sett.foreing_lang
                sett.update()
                self.init()
        def clear_clicked(self):
                self.answer.clear()
        def init(self):  
                self.clear_clicked()  
                self.verb = verb(self.word_count)
                info = verb.get_level()
                self.info.setText(f"{info[0]} | Level {info[1]}")
                ru_0=self.verb.ru_verb
                ru_1 = self.verb.ru_complete_verb.split(";")
                native_lang = [ver[2] for ver in lang(self.native,self.verb.id).get()]
                foreing_lang =[ver[2] for ver in lang(self.foreing,self.verb.id).get()]     
                if int(self.verb.point)<250:
                        if int(self.verb.point)<=100:
                                self.new_lang.setText(ru_0)
                                self.new_lang_extra.setText(" / ".join(ru_1))
                                self.native_lang_verb.setText("/".join(native_lang))
                                self.foreing_lang_verb.setText("/".join(foreing_lang))
                        else:
                                self.ru_verb.setText(ru_0)
                                self.new_lang_extra.setText(" / ".join(ru_1))
                        self.answers = native_lang+foreing_lang   
                else:
                        self.native_lang_verb.setText("/".join(native_lang))
                        self.foreing_lang_verb.setText("/".join(foreing_lang))
                        self.answers = ru_1
        def clicked_submit(self):
                answer = self.answer.text()
                if answer in self.answers and self.verb:
                        self.verb.point = int(self.verb.point)+10
                        self.verb.last_date = str(datetime.datetime.now())[:10]
                        self.verb.update()
                #else:
                #        self.verb.point = int(self.verb.point)-10 if int(self.verb.point)>=10 else 0
                #        self.verb.last_date = str(datetime.datetime.now())[:10]
                #        self.verb.update()   
                        self.init()
        def skipclicked(self):
                self.verb.point = int(self.verb.point)+100
                self.verb.last_date = str(datetime.datetime.now())[:10]
                self.verb.update()
                self.clear_clicked()
                self.init()
        def help_native_clicked(self):
                native_lang = [ver[2] for ver in lang(self.native,self.verb.id).get()]
                self.native_lang_verb.setText("/".join(native_lang))
        def help_foreign_clicked(self):
                foreing_lang =[ver[2] for ver in lang(self.foreing,self.verb.id).get()]
                self.foreing_lang_verb.setText("/".join(foreing_lang))

        def init_word(self):
                self.word = Word(self.word_count)
                trans_word = Word_trans(0,self.word.id)
                info = self.word.get_info()
                self.clear_word_clicked() 
                self.info_word.setText(f"{info[0]} | Level {info[1]}")
                new_lang                = self.word.word.split(";")
                native_lang             = trans_word.word.split(";")
                new_lang_extra          = self.word.extra.split(";")
                native_lang_extra       = trans_word.extra.split(";")  

                if int(self.word.point)<250:
                        if int(self.word.point)<=100:
                                self.new_lang_word.setText(", ".join(new_lang))
                                self.native_lang_word.setText(", ".join(native_lang))
                                self.new_lang_extra_word.setText(" | ".join(new_lang_extra))
                                self.native_lang_extra_word.setText(" | ".join(native_lang_extra))
                                
                        else:
                                self.new_lang_word.setText(", ".join(new_lang))
                                self.new_lang_extra_word.setText(" | ".join(new_lang_extra))
                        self.word_answers = native_lang+native_lang_extra 
                else:
                        self.native_lang_word.setText(", ".join(native_lang))
                        self.native_lang_word.setText(" | ".join(native_lang_extra))
                        self.word_answers = native_lang+native_lang_extra
                self.answer.clear()
        def clear_word_clicked(self):
                self.answer_word.clear()
        def skip_word_clicked(self):
                self.word.point = (int(self.word.point)/100)*100+100
                self.word.update()
                self.init_word()
                self.clear_word_clicked()
        def help_native_word_clicked(self):
                pass#self.new_lang_extra_word.setText("")
        def help_foreign_word_clicked(self):
                pass#self.native_lang_extra_word.setText("")
        def answer_word_pressed(self):
                answer = self.answer_word.text()
                if answer in self.word_answers and self.word:
                        self.word.point = int(self.word.point)+10
                        self.word.last_time = str(datetime.datetime.now())[:10]
                        self.word.update()
                        self.init_word() 


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
 