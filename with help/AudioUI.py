import pyaudio
from scipy import signal
import numpy as np
import queue
import pyqtgraph as pg
from PySide6 import QtCore
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
        self.widget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(140, 60, 891, 71))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 50pt \"Bahnschrift SemiBold Condensed\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalSliderPlayer = QSlider(self.widget)
        self.horizontalSliderPlayer.setObjectName(u"horizontalSliderPlayer")
        self.horizontalSliderPlayer.setGeometry(QtCore.QRect(130, 250, 671, 41))
        self.horizontalSliderPlayer.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalSliderPlayer.setOrientation(QtCore.Qt.Horizontal)
        self.widget_2 = pg.PlotWidget(self.widget)  # Replace QWidget with pg.PlotWidget
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QtCore.QRect(80, 390, 1000, 231))
        self.widget_2.setBackground('k')  # Set background color to black
        self.labelTimer = QLabel(self.widget)
        self.labelTimer.setObjectName(u"labelTimer")
        self.labelTimer.setGeometry(QtCore.QRect(900, 220, 150, 50))
        font = QFont()
        font.setPointSize(25)
        self.labelTimer.setFont(font)
        self.labelTimer.setAlignment(QtCore.Qt.AlignCenter)
        self.toolButtonPlay = QToolButton(self.widget)
        self.toolButtonPlay.setObjectName(u"toolButtonPlay")
        self.toolButtonPlay.setGeometry(QtCore.QRect(880, 300, 50, 50))
        self.toolButtonPlay.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 127);\n"
"border-radius : 20px")
        self.toolButtonPause = QToolButton(self.widget)
        self.toolButtonPause.setObjectName(u"toolButtonPause")
        self.toolButtonPause.setGeometry(QtCore.QRect(950, 300, 50, 50))
        self.toolButtonPause.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 127);\n"
"border-radius : 20px")
        self.toolButtonStop = QToolButton(self.widget)
        self.toolButtonStop.setObjectName(u"toolButtonStop")
        self.toolButtonStop.setGeometry(QtCore.QRect(1020, 300, 50, 50))
        self.toolButtonStop.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 127);\n"
"border-radius : 20px")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen_Music)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Music.setText(QCoreApplication.translate("MainWindow", u"Open Music", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Audio Player and Spectrogram Preview", None))
        self.labelTimer.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.toolButtonPlay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.toolButtonPause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.toolButtonStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))