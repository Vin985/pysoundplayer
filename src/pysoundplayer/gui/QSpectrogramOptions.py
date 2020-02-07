from functools import partial

from PySide2 import QtCore, QtWidgets

from .ui.QSpectrogramOptions_ui import Ui_SpectrogramOptions
from .settings import SoundPlayerSettings
from ..spectrogram.spectrogram import Spectrogram
from ..spectrogram.image import ImageGenerator


class QSpectrogramOptions(QtWidgets.QWidget, Ui_SpectrogramOptions):

    update_spectrogram = QtCore.Signal()
    update_image = QtCore.Signal()

    def __init__(self, parent, settings=None):
        super().__init__(parent)
        self._settings = None
        self.setupUi(self)
        self.update_option = self.map_update_option_functions()
        self.update_ui = self.map_update_ui_functions()
        self.link_events()

        if settings:
            self.settings = settings

    @property
    def options(self):
        return self._settings.options

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, settings):
        if settings:
            self._settings = settings
            self.init_values()

    def link_events(self):
        # Spectrogram
        self.cb_pcen.stateChanged.connect(self.use_pcen)
        self.cb_remove_noise.stateChanged.connect(
            partial(self.update,
                    "remove_noise",
                    "checkbox",
                    SoundPlayerSettings.GROUP_SPECTROGRAM))
        self.cb_normalize.stateChanged.connect(
            partial(self.update,
                    "normalize",
                    "checkbox",
                    SoundPlayerSettings.GROUP_SPECTROGRAM))
        self.cb_todb.stateChanged.connect(
            partial(self.update,
                    "to_db",
                    "checkbox",
                    SoundPlayerSettings.GROUP_SPECTROGRAM))
        self.combo_fft.currentTextChanged.connect(
            partial(self.update,
                    "n_fft",
                    "combobox",
                    SoundPlayerSettings.GROUP_SPECTROGRAM))
        self.combo_scale.currentTextChanged.connect(
            partial(self.update,
                    "scale",
                    "combobox",
                    SoundPlayerSettings.GROUP_SPECTROGRAM))
        self.combo_window.currentTextChanged.connect(
            partial(self.update,
                    "window",
                    "combobox",
                    SoundPlayerSettings.GROUP_SPECTROGRAM))

        # Display
        self.cb_invert_colors.stateChanged.connect(
            partial(self.update,
                    "invert_colors",
                    "checkbox",
                    SoundPlayerSettings.GROUP_IMAGE))
        self.spin_pix_in_sec.valueChanged.connect(
            partial(self.update,
                    "pixels_in_sec",
                    "spinbox",
                    SoundPlayerSettings.GROUP_IMAGE))
        self.spin_height.valueChanged.connect(
            partial(self.update,
                    "height",
                    "spinbox",
                    SoundPlayerSettings.GROUP_IMAGE))
        self.combo_color_map.currentTextChanged.connect(
            partial(self.update,
                    "color_map",
                    "combobox",
                    SoundPlayerSettings.GROUP_IMAGE))
        self.slider_contrast.valueChanged.connect(
            partial(self.update,
                    "contrast",
                    "slider",
                    SoundPlayerSettings.GROUP_IMAGE))

    # associate a fonction to update a value from a specific ui element
    # Used for updating the ui from the settings
    def map_update_ui_functions(self):
        res = {"to_db": partial(self.update_checkbox, self.cb_todb),
               "pcen": partial(self.update_checkbox, self.cb_pcen),
               "remove_noise": partial(self.update_checkbox, self.cb_remove_noise),
               "invert_colors": partial(self.update_checkbox, self.cb_invert_colors),
               "pixels_in_sec": partial(self.update_spinbox, self.spin_pix_in_sec),
               "height": partial(self.update_spinbox, self.spin_height),
               "scale": partial(self.update_combobox, self.combo_scale, Spectrogram.ACCEPTED_VALUES["scale"]),
               "n_fft": partial(self.update_combobox, self.combo_fft, Spectrogram.ACCEPTED_VALUES["n_fft"]),
               "window": partial(self.update_combobox, self.combo_window, Spectrogram.ACCEPTED_VALUES["window"]),
               "color_map": partial(self.update_combobox, self.combo_color_map, ImageGenerator.ACCEPTED_VALUES["color_map"]),
               "contrast": partial(self.update_slider, self.slider_contrast)
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

    def map_update_option_functions(self):
        res = {"checkbox": self.update_from_checkbox,
               "spinbox": self.update_from_spinbox,
               "combobox": self.update_from_combobox,
               "slider": self.update_from_slider}
        return res

    def update(self, option, ui_element, opt_group, value):
        self.update_option[ui_element](option, opt_group, value)
        # emit signal to recompute image or spectrogram
        getattr(self, "update_" + opt_group).emit()

    def update_from_checkbox(self, option, opt_group, value):
        self.options[opt_group][option] = (
            value == QtCore.Qt.CheckState.Checked)

    def update_from_spinbox(self, option, opt_group, value):
        self.options[opt_group][option] = value

    def update_from_combobox(self, option, opt_group, value):
        self.options[opt_group][option] = value

    def update_from_slider(self, option, opt_group, value):
        self.options[opt_group][option] = value

    def use_pcen(self, value):
        use_pcen = (value == QtCore.Qt.CheckState.Checked)
        self.cb_remove_noise.setEnabled(not use_pcen)
        self.update("pcen", "checkbox",
                    SoundPlayerSettings.GROUP_SPECTROGRAM, value)

    def update_checkbox(self, checkbox, value):
        checkbox.setChecked(value)

    def update_spinbox(self, spinbox, value):
        spinbox.setValue(value)

    def update_slider(self, slider, value):
        slider.setValue(value)

    def update_combobox(self, combobox, choices, value):
        if combobox.count() == 0:
            combobox.insertItems(0, choices)
        combobox.setCurrentText(str(value))

    def init_values(self):
        for opt_type, options in self.options.items():
            for key, value in options.items():
                if key in self.update_ui:
                    self.update_ui[key](value)
                else:
                    print("Option not mapped: " + key)
