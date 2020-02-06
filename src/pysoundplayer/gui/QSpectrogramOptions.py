from PySide2 import QtWidgets, QtCore
from .ui.QSpectrogramOptions_ui import Ui_SpectrogramOptions
from functools import partial
from ..spectrogram.spectrogram import Spectrogram
from ..spectrogram.image import ImageGenerator
from .settings import SoundPlayerSettings


class QSpectrogramOptions(QtWidgets.QWidget, Ui_SpectrogramOptions):

    update_spectrogram = QtCore.Signal()
    update_image = QtCore.Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.settings = SoundPlayerSettings()
        self.setupUi(self)
        self.update_option = self.map_update_option_functions()
        self.update_ui = self.map_update_ui_functions()
        self.link_events()
        self.init_values()

    @property
    def options(self):
        return self.settings.options

    def link_events(self):
        # Spectrogram
        self.cb_pcen.stateChanged.connect(self.use_pcen)
        self.cb_remove_noise.stateChanged.connect(partial(self.update,
                                                          "remove_noise",
                                                          "checkbox",
                                                          self.settings.GROUP_SPECTROGRAM))
        self.cb_normalize.stateChanged.connect(partial(self.update,
                                                       "normalize",
                                                       "checkbox",
                                                       self.settings.GROUP_SPECTROGRAM))
        self.cb_todb.stateChanged.connect(partial(self.update,
                                                  "to_db",
                                                  "checkbox",
                                                  self.settings.GROUP_SPECTROGRAM))

        # Display
        self.cb_invert.stateChanged.connect(
            partial(self.update, "invert", "cb", self.settings.GROUP_IMAGE))

    def update_values(self):
        pass

    # associate a fonction to update a value from a specific ui element
    def map_update_option_functions(self):
        res = {"checkbox": self.update_from_checkbox}
        return res

    def map_update_ui_functions(self):
        res = {"to_db": partial(self.update_checkbox, self.cb_todb),
               "pcen": partial(self.update_checkbox, self.cb_pcen),
               "remove_noise": partial(self.update_checkbox, self.cb_remove_noise),
               "invert_colors": partial(self.update_checkbox, self.cb_invert)
               }
        return res
        # self.update_ui["contrast"] = self.slider_contrast
        # self.update_ui["height"] = self.spin_height
        # self.update_ui["pixels_in_sec"] = self.spin_pix_in_sec
        # self.update_ui["n_fft"] = self.combo_fft

        # DEFAULT_OPTIONS = {"n_fft": 512, "to_db": True, "pcen": False,
        #                    "remove_noise": None, "normalize": False,
        #                    "hop_length": None, "window": 'hann', "scale": "Linear",
        #                    "nr_hist_rel_size": 2, "nr_N": 0.1, "nr_window_smoothing": 5}

    def update(self, option, ui_element, opt_group, value):
        self.update_option[ui_element](option, opt_group, value)
        # emit signal to recompute image or spectrogram
        getattr(self, "update_" + opt_group).emit()

    def update_from_checkbox(self, option, opt_group, value):
        self.options[opt_group][option] = (
            value == QtCore.Qt.CheckState.Checked)
        print(self.options[opt_group])

    def use_pcen(self, value):
        use_pcen = (value == QtCore.Qt.CheckState.Checked)
        self.cb_remove_noise.setEnabled(not use_pcen)
        self.update_from_checkbox(
            "pcen", self.settings.GROUP_SPECTROGRAM, value)

    def update_checkbox(self, checkbox, value):
        checkbox.setChecked(value)

    def update_combobox(self, combobox, value):
        pass

    def init_values(self):
        for opt_type, options in self.options.items():
            for key, value in options.items():
                if key in self.update_ui:
                    print(key)
                    print(value)
                    self.update_ui[key](value)
                    # self.update_ui[key](value)
                else:
                    print("Option not mapped: " + key)
