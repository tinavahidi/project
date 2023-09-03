import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from AudioUI import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QTime


import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import queue
import numpy as np

class MplCanvas(FigureCanvas):
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		super(MplCanvas, self).__init__(fig)
		fig.tight_layout()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.toolButtonPlay.setEnabled(False)

        self.player = QMediaPlayer()
        self.audio = QAudioOutput()

        self.player.setAudioOutput(self.audio)

        self.ui.actionOpen_Music.triggered.connect(self.open_music)
        self.ui.toolButtonPlay.clicked.connect(self.Play_music)
        self.ui.toolButtonPause.clicked.connect(self.Pause_music)
        self.ui.toolButtonStop.clicked.connect(self.Stop_music)
        self.ui.horizontalSliderPlayer.sliderMoved.connect(self.PlaySliderChanged)

        # connect media player signals
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.durationChanged)


    def open_music(self):
        FileName, _ = QFileDialog.getOpenFileName(self, "Open Music")

        if FileName != '':
            self.player.setSource(QUrl.fromLocalFile(FileName))
            self.ui.toolButtonPlay.setEnabled(True)

    def Play_music(self):
        if self.player.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def Pause_music(self):
        self.player.pause()

    def Stop_music(self):
        self.player.stop()

    def position_changed(self, position):
        if (self.ui.horizontalSliderPlayer.maximum() != self.player.duration()):
            self.ui.horizontalSliderPlayer.setMaximum(self.player.duration())

        self.ui.horizontalSliderPlayer.setValue(position)

        seconds = (position / 1000) % 60
        minutes = (position / 60000) % 60
        hours = (position / 2600000) % 24

        time = QTime(hours, minutes, seconds)
        self.ui.labelTimer.setText(time.toString())

    def durationChanged(self, duration):
        self.ui.horizontalSliderPlayer.setRange(0, duration)

    def PlaySliderChanged(self, position):
        self.player.setPosition(position)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
