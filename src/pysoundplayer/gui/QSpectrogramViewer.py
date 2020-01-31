from PIL import ImageDraw, ImageQt
from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import (QGraphicsPixmapItem, QGraphicsScene,
                               QGraphicsTextItem, QMenu, QMessageBox, QWidget)
from ..spectrogram.image import ImageGenerator
from .ui.QSpectrogramViewer_ui import Ui_SpectrogramViewer


class QSpectrogramViewer(QtWidgets.QWidget, Ui_SpectrogramViewer):

    def __init__(self, parent=None, audio=None, spectrogram_options=None, image_options=None):
        super().__init__(parent)
        self.setupUi(self)
        self.bg_image = None
        self.spectrogram_scene = QGraphicsScene(self)

        self._audio = None
        self._spectrogram = None

        self.spectrogram_options = {} if spectrogram_options is None else spectrogram_options
        self.image_generator = ImageGenerator(image_options)

        self.audio = audio
        self.setup_graphics_view()

    @property
    def audio(self):
        return self._audio

    @audio.setter
    def audio(self, audio):
        if audio is not None:
            self._audio = audio
            self.spectrogram = audio.get_spectrogram(
                self.spectrogram_options)

    @property
    def spectrogram(self):
        return self._spectrogram

    @spectrogram.setter
    def spectrogram(self, spectrogram):
        self._spectrogram = spectrogram
        self.update_spectrogram()

    def setup_graphics_view(self):
        self.spectrogram_view.setScene(self.spectrogram_scene)
        self.spectrogram_view.setMouseTracking(True)

    def sec2pixels(self, sec, to_int=True):
        pix = 299 * sec / 1.5
        if to_int:
            return int(pix)
        return pix

    def update_spectrogram(self):
        # TODO: externalize ratio pixel/duration
        # TODO: save image somewhere
        im = self.image_generator.spec2img(self.spectrogram.spec, size=(
            self.sec2pixels(self.audio.duration), 299))
        # TODO: change events when checkbox is checked
        # if self.checkbox_draw_events.isChecked():
        #     im = self.draw_events(im, max_duration)
        img = ImageQt.ImageQt(im)
        pixmap = QPixmap.fromImage(img)

        # Change Qt array to a Qt graphic
        self.bg_image = QGraphicsPixmapItem(pixmap)
        self.spectrogram_scene.clear()
        self.spectrogram_scene.addItem(self.bg_image)
        # Ensure spectrogram graphic is displayed as background
        self.bg_image.setZValue(-100)
        self.bg_image.setPos(0, 0)

    def display_text(self, text):
        text_item = QGraphicsTextItem()
        text_item.setPos(150, 100)
        text_item.setPlainText(text)
        self.spectrogram_scene.clear()
        self.spectrogram_scene.addItem(text_item)
