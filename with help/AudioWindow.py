import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from AudioUI import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QTime
import pyaudio
from scipy import signal
import numpy as np
import queue
import pyqtgraph as pg
from PySide6 import QtCore

from PySide6.QtCore import QUrl, QTime
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from pydub import AudioSegment
import tempfile

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from AudioUI import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QTime
import pyaudio
from scipy import signal
import numpy as np
import queue
import pyqtgraph as pg
from PySide6 import QtCore


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
        self.ui.horizontalSliderPlayer.sliderMoved.connect(
            self.PlaySliderChanged)
        self.ui.toolButtonPlay.clicked.connect(self.update_spectrogram)

        # Connect media player signals
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.durationChanged)

        self.chunk_size = 2048
        self.sample_rate = 44100
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size,
        )

        self.spec_data = np.zeros((512, int(self.chunk_size / 2) + 1))

        self.spec_img = pg.PlotWidget(self.ui.widget_2)
        self.spec_img.setMouseEnabled(x=False, y=False)
        self.spec_img.hideAxis("bottom")
        self.spec_img.hideAxis("left")
        self.spec_img.setRange(
            xRange=[0, np.log(self.sample_rate / 2)], yRange=[0, self.sample_rate / 2], padding=0
        )

        self.spec_img_img = pg.ImageItem()
        self.spec_img.addItem(self.spec_img_img)
        self.spec_img_img.setLevels([-40, 40])

        self.spec_data_queue = queue.Queue(maxsize=10)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_spectrogram)
        self.timer.start(50)

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
        if self.ui.horizontalSliderPlayer.maximum() != self.player.duration():
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

    def update_spectrogram(self):
        data = self.stream.read(self.chunk_size)
        data = np.frombuffer(data, dtype=np.int16)
        data = signal.detrend(data)

        f, t, spec = signal.spectrogram(
            data, self.sample_rate, window='hamming', nperseg=512, noverlap=256)

        if self.spec_data_queue.full():
            self.spec_data_queue.get()

        self.spec_data_queue.put(spec)

        self.spec_data = np.zeros_like(spec)  # Adjust the size of spec_data

        for spec in self.spec_data_queue.queue:
            self.spec_data += spec

        self.spec_data /= self.spec_data_queue.qsize()

        self.spec_data = 10 * np.log10(self.spec_data)

        self.spec_img_img.setImage(self.spec_data)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
