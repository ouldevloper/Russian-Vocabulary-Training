# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMhVNYv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(552, 552)
        MainWindow.setMinimumSize(QSize(552, 552))
        MainWindow.setMaximumSize(QSize(552, 552))
        MainWindow.setStyleSheet(u"color:white;\n"
"background-color: rgb(61, 56, 70);\n"
"margin:0px;\n"
"padding:0px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(534, 534))
        self.stackedWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.layoutWidget = QWidget(self.stackedWidgetPage1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 20, 531, 471))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ru_verb = QLabel(self.layoutWidget)
        self.ru_verb.setObjectName(u"ru_verb")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ru_verb.setFont(font)
        self.ru_verb.setStyleSheet(u"margin:10px;\n"
"background-color: rgb(153, 193, 241);\n"
"border-radius: 10px;")
        self.ru_verb.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ru_verb, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.ru_verb_complete = QLabel(self.layoutWidget)
        self.ru_verb_complete.setObjectName(u"ru_verb_complete")
        self.ru_verb_complete.setFont(font)
        self.ru_verb_complete.setStyleSheet(u"background-color: rgb(249, 240, 107);\n"
"margin:10px;\n"
"border-radius:10px;")
        self.ru_verb_complete.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ru_verb_complete)

        self.native_lang_verb = QLabel(self.layoutWidget)
        self.native_lang_verb.setObjectName(u"native_lang_verb")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.native_lang_verb.setFont(font1)
        self.native_lang_verb.setLayoutDirection(Qt.RightToLeft)
        self.native_lang_verb.setStyleSheet(u"background-color: rgb(255, 163, 72);\n"
"border-radius:10px;\n"
"margin:10px;")
        self.native_lang_verb.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.native_lang_verb)

        self.foreing_lang_verb = QLabel(self.layoutWidget)
        self.foreing_lang_verb.setObjectName(u"foreing_lang_verb")
        self.foreing_lang_verb.setFont(font1)
        self.foreing_lang_verb.setStyleSheet(u"background-color: rgb(246, 97, 81);\n"
"border-radius:10px;\n"
"margin:10px;")
        self.foreing_lang_verb.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.foreing_lang_verb)

        self.help_native = QPushButton(self.stackedWidgetPage1)
        self.help_native.setObjectName(u"help_native")
        self.help_native.setGeometry(QRect(510, 260, 21, 21))
        self.help_native.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"Cantarell\";\n"
"background-color: rgb(98, 160, 234);\n"
"\n"
"")
        self.clear = QPushButton(self.stackedWidgetPage1)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(470, 500, 51, 27))
        self.clear.setMaximumSize(QSize(70, 100))
        self.clear.setStyleSheet(u"background-color: rgb(46, 194, 126);\n"
"border-raduis:10px;\n"
"color:white;\n"
"border-radius:10px;")
        self.skip = QPushButton(self.stackedWidgetPage1)
        self.skip.setObjectName(u"skip")
        self.skip.setGeometry(QRect(510, 20, 21, 21))
        self.skip.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"Cantarell\";\n"
"background-color: rgb(245, 194, 17);\n"
"\n"
"")
        self.answer = QLineEdit(self.stackedWidgetPage1)
        self.answer.setObjectName(u"answer")
        self.answer.setGeometry(QRect(0, 500, 481, 27))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer.sizePolicy().hasHeightForWidth())
        self.answer.setSizePolicy(sizePolicy)
        self.answer.setMaximumSize(QSize(16777215, 16777215))
        self.answer.setStyleSheet(u"background-color: rgb(154, 153, 150);\n"
"border-radius:5px;\n"
"margin-left:10px;")
        self.help_foreign = QPushButton(self.stackedWidgetPage1)
        self.help_foreign.setObjectName(u"help_foreign")
        self.help_foreign.setGeometry(QRect(510, 380, 21, 21))
        self.help_foreign.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"Cantarell\";\n"
"background-color: rgb(98, 160, 234);\n"
"\n"
"")
        self.next = QPushButton(self.stackedWidgetPage1)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(500, -10, 31, 21))
        self.next.setStyleSheet(u"color:white;\n"
"background-color: rgb(61, 56, 70);\n"
"margin:0px;\n"
"padding:0px;")
        icon = QIcon()
        icon.addFile(u"next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next.setIcon(icon)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.groupBox_2 = QGroupBox(self.stackedWidgetPage2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 50, 521, 211))
        self.layoutWidget_5 = QWidget(self.groupBox_2)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(130, 100, 331, 43))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.foreign_lang = QComboBox(self.layoutWidget_5)
        self.foreign_lang.addItem("")
        self.foreign_lang.addItem("")
        self.foreign_lang.addItem("")
        self.foreign_lang.addItem("")
        self.foreign_lang.setObjectName(u"foreign_lang")
        self.foreign_lang.setStyleSheet(u"QComboBox{\n"
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
        self.foreign_lang.setIconSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.foreign_lang)

        self.layoutWidget_6 = QWidget(self.groupBox_2)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(130, 50, 331, 53))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_6)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.native_lang = QComboBox(self.layoutWidget_6)
        self.native_lang.addItem("")
        self.native_lang.addItem("")
        self.native_lang.addItem("")
        self.native_lang.addItem("")
        self.native_lang.setObjectName(u"native_lang")
        self.native_lang.setStyleSheet(u"QComboBox{\n"
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
        self.native_lang.setIconSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.native_lang)

        self.save_lang = QPushButton(self.groupBox_2)
        self.save_lang.setObjectName(u"save_lang")
        self.save_lang.setGeometry(QRect(350, 150, 111, 27))
        self.save_lang.setStyleSheet(u"background-color:#007fff;")
        self.groupBox = QGroupBox(self.stackedWidgetPage2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(9, 270, 521, 191))
        self.groupBox.setStyleSheet(u"border-bottom-color: rgb(255, 255, 255);")
        self.layoutWidget_3 = QWidget(self.groupBox)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(130, 90, 331, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.words_run = QSpinBox(self.layoutWidget_3)
        self.words_run.setObjectName(u"words_run")
        self.words_run.setMaximumSize(QSize(16777215, 30))
        self.words_run.setStyleSheet(u"background-color:   rgb(87, 96, 134);\n"
"color:                      rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"margin:0x;\n"
"padding:0px;")

        self.horizontalLayout_3.addWidget(self.words_run)

        self.layoutWidget_4 = QWidget(self.groupBox)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(130, 40, 331, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.nickname = QLineEdit(self.layoutWidget_4)
        self.nickname.setObjectName(u"nickname")
        self.nickname.setMaximumSize(QSize(16777215, 30))
        self.nickname.setStyleSheet(u"background-color:   rgb(87, 96, 134);\n"
"color:                      rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"margin:0x;\n"
"padding:0px;")

        self.horizontalLayout_4.addWidget(self.nickname)

        self.save_user = QPushButton(self.groupBox)
        self.save_user.setObjectName(u"save_user")
        self.save_user.setGeometry(QRect(350, 140, 111, 27))
        self.save_user.setStyleSheet(u"background-color:#007fff;")
        self.groupBox_3 = QGroupBox(self.stackedWidgetPage2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(9, 533, 527, 50))
        self.groupBox_3.setMaximumSize(QSize(16777215, 50))
        self.back = QPushButton(self.stackedWidgetPage2)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(500, 0, 31, 21))
        self.back.setStyleSheet(u"color:white;\n"
"background-color: rgb(61, 56, 70);\n"
"margin:0px;\n"
"padding:0px;")
        icon1 = QIcon()
        icon1.addFile(u"back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back.setIcon(icon1)
        self.stackedWidget.addWidget(self.stackedWidgetPage2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"500 Comman Russian Verbs", None))
        self.ru_verb.setText("")
        self.ru_verb_complete.setText("")
        self.native_lang_verb.setText("")
        self.foreing_lang_verb.setText("")
        self.help_native.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"  C", None))
        self.skip.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.help_foreign.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.next.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Language Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"  Native Lnaguage", None))
        self.foreign_lang.setItemText(0, QCoreApplication.translate("MainWindow", u"en", None))
        self.foreign_lang.setItemText(1, QCoreApplication.translate("MainWindow", u"ar", None))
        self.foreign_lang.setItemText(2, QCoreApplication.translate("MainWindow", u"fr", None))
        self.foreign_lang.setItemText(3, QCoreApplication.translate("MainWindow", u"ru", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"  Native Lnaguage", None))
        self.native_lang.setItemText(0, QCoreApplication.translate("MainWindow", u"en", None))
        self.native_lang.setItemText(1, QCoreApplication.translate("MainWindow", u"ar", None))
        self.native_lang.setItemText(2, QCoreApplication.translate("MainWindow", u"fr", None))
        self.native_lang.setItemText(3, QCoreApplication.translate("MainWindow", u"ru", None))

        self.save_lang.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"User Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"  words/run", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"  Nick name", None))
        self.save_user.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_3.setTitle("")
        self.back.setText("")
    # retranslateUi


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
