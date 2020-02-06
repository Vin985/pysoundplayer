from PIL import ImageQt
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import (QGraphicsPixmapItem, QGraphicsScene,
                               QGraphicsTextItem)
from ..spectrogram.image import ImageGenerator
from .ui.QSpectrogramViewer_ui import Ui_SpectrogramViewer
from .event_filters import SpectrogramMouseFilter


class QSpectrogramViewer(QtWidgets.QWidget, Ui_SpectrogramViewer):

    seek = QtCore.Signal(float)

    def __init__(self, parent=None, audio=None, spectrogram_options=None, image_options=None):
        super().__init__(parent)
        self.setupUi(self)
        self.bg_image = None
        self.spectrogram_scene = QGraphicsScene(self)

        self._audio = None
        self._spectrogram = None
        self.sound_marker = None
        self.yscale = 1

        self.spectrogram_options = {} if spectrogram_options is None else spectrogram_options
        self.image_options = {} if image_options is None else image_options
        self.image_generator = ImageGenerator(image_options)

        self.audio = audio
        self.setup_graphics_view()
        self.define_shortcuts()
        self.install_filters()

    def setup_graphics_view(self):
        self.spectrogram_view.setScene(self.spectrogram_scene)

    def define_shortcuts(self):
        QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Plus),
                            self, self.zoom_in)
        QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Minus),
                            self, self.zoom_out)

    def install_filters(self):
        self.mouse_filter = SpectrogramMouseFilter(self)
        self.spectrogram_scene.installEventFilter(self.mouse_filter)

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

    def update_spectrogram(self):
        # TODO: externalize ratio pixel/duration
        # TODO: save image somewhere
        im = self.image_generator.spec2img(self.spectrogram)
        # TODO: change events when checkbox is checked
        # if self.checkbox_draw_events.isChecked():
        #     im = self.draw_events(im, max_duration)
        img = ImageQt.ImageQt(im)
        pixmap = QtGui.QPixmap.fromImage(img)

        # Change Qt array to a Qt graphic
        self.bg_image = QGraphicsPixmapItem(pixmap)
        self.spectrogram_scene.clear()
        self.spectrogram_scene.addItem(self.bg_image)
        # Ensure spectrogram graphic is displayed as background
        self.bg_image.setZValue(-100)
        self.bg_image.setPos(0, 0)
        self.update_sound_marker(0)

    def display_text(self, text):
        text_item = QGraphicsTextItem()
        text_item.setPos(150, 100)
        text_item.setPlainText(text)
        self.spectrogram_scene.clear()
        self.spectrogram_scene.addItem(text_item)

    def update_sound_marker(self, position_sec):
        # 100 # multiply by step-size in SpecGen()
        marker_pos = self.image_generator.sec2pixels(position_sec)
        line = QtCore.QLineF(marker_pos, 0, marker_pos,
                             self.image_generator["height"])
        if not self.sound_marker:
            penCol = QtGui.QColor()
            penCol.setRgb(255, 0, 0)
            self.sound_marker = self.spectrogram_scene.addLine(
                line, QtGui.QPen(penCol))
        else:
            self.sound_marker.setLine(line)

        self.spectrogram_scene.update()

        # if self.spectrogram_options.follow():
        #     self.scrollingWithoutUser = True
        #     self.scrollView.centerOn(markerPos, self.viewCenter.y())
        #     self.scrollingWithoutUser = False
        #     self.setZoomBoundingBox(updateCenter=False)

    def zoom(self, scale, scene_pos=None):
        self.yscale *= scale
        self.spectrogram_view.scale(scale, scale)
        if scene_pos:
            self.spectrogram_view.centerOn(scene_pos)

    def zoom_in(self):
        self.zoom(1.5)

    def zoom_out(self):
        self.zoom(0.75)

    def seek_sound(self, pos):
        self.seek.emit(self.image_generator.pixels2sec(pos))
