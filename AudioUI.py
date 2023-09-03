# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AudioUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QSlider, QStatusBar,
    QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet(u"QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0.244, y1:0.471591, x2:1, y2:1, stop:0 rgba(255, 85, 127, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.actionOpen_Music = QAction(MainWindow)
        self.actionOpen_Music.setObjectName(u"actionOpen_Music")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1200, 800))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 60, 891, 71))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 50pt \"Bahnschrift SemiBold Condensed\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.horizontalSliderPlayer = QSlider(self.widget)
        self.horizontalSliderPlayer.setObjectName(u"horizontalSliderPlayer")
        self.horizontalSliderPlayer.setGeometry(QRect(130, 250, 671, 41))
        self.horizontalSliderPlayer.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalSliderPlayer.setOrientation(Qt.Horizontal)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(80, 390, 1000, 231))
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.labelTimer = QLabel(self.widget)
        self.labelTimer.setObjectName(u"labelTimer")
        self.labelTimer.setGeometry(QRect(900, 220, 150, 50))
        font = QFont()
        font.setPointSize(25)
        self.labelTimer.setFont(font)
        self.labelTimer.setAlignment(Qt.AlignCenter)
        self.toolButtonPlay = QToolButton(self.widget)
        self.toolButtonPlay.setObjectName(u"toolButtonPlay")
        self.toolButtonPlay.setGeometry(QRect(880, 300, 50, 50))
        self.toolButtonPlay.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 127);\n"
"border-radius : 20px")
        self.toolButtonPause = QToolButton(self.widget)
        self.toolButtonPause.setObjectName(u"toolButtonPause")
        self.toolButtonPause.setGeometry(QRect(950, 300, 50, 50))
        self.toolButtonPause.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 127);\n"
"border-radius : 20px")
        self.toolButtonStop = QToolButton(self.widget)
        self.toolButtonStop.setObjectName(u"toolButtonStop")
        self.toolButtonStop.setGeometry(QRect(1020, 300, 50, 50))
        self.toolButtonStop.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 127);\n"
"border-radius : 20px")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen_Music)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Music.setText(QCoreApplication.translate("MainWindow", u"Open Music", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Audio Player and Spectrogram Preview", None))
        self.labelTimer.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.toolButtonPlay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.toolButtonPause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.toolButtonStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

