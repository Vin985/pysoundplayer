from functools import partial

from .QOptionsWidget import QOptionsWidget
from .settings import SoundPlayerSettings
from ..spectrogram.image import ImageOptions
from .ui.QImageOptions_ui import Ui_QImageOptions


class QImageOptions(QOptionsWidget, Ui_QImageOptions):

    def __init__(self, parent, options=None):
        super().__init__(parent, self, options)
        self.group = ImageOptions.TYPE

    def link_events(self):
        self.cb_invert_colors.stateChanged.connect(partial(self.update,
                                                           "invert_colors",
                                                           checkbox=True))
        self.spin_pix_in_sec.valueChanged.connect(partial(self.update,
                                                          "pixels_in_sec"))
        self.spin_height.valueChanged.connect(partial(self.update,
                                                      "height"))
        self.combo_color_map.currentTextChanged.connect(partial(self.update,
                                                                "color_map"))
        self.slider_contrast.valueChanged.connect(partial(self.update,
                                                          "contrast"))

    # associate a fonction to update a value from a specific ui element
    # Used for updating the ui from the settings
    def map_update_ui_functions(self):
        res = {
            "invert_colors": partial(self.update_checkbox, self.cb_invert_colors),
            "pixels_in_sec": partial(self.update_spinbox, self.spin_pix_in_sec),
            "height": partial(self.update_spinbox, self.spin_height),
            "color_map": partial(self.update_combobox, self.combo_color_map,
                                 ImageOptions.ACCEPTED_VALUES["color_map"]),
            "contrast": partial(self.update_slider, self.slider_contrast)
        }
        return res
