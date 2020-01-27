from PySide2 import QtWidgets


class JumpSlider(QtWidgets.QSlider):

    def mousePressEvent(self, ev):
        """ Jump to click position """
        self.setValue(QtWidgets.QStyle.sliderValueFromPosition(
            self.minimum(), self.maximum(), ev.x(), self.width()))

    def mouseMoveEvent(self, ev):
        """ Jump to pointer position while moving """
        self.setValue(QtWidgets.QStyle.sliderValueFromPosition(
            self.minimum(), self.maximum(), ev.x(), self.width()))
