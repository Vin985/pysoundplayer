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
                    SoundPlayerSettings.GROUP_SPECTROGRAM,
                    checkbox=True))
        self.cb_normalize.stateChanged.connect(
            partial(self.update,
                    "normalize",
                    SoundPlayerSettings.GROUP_SPECTROGRAM,
                    checkbox=True))
        self.cb_todb.stateChanged.connect(
            partial(self.update,
                    "to_db",
                    SoundPlayerSettings.GROUP_SPECTROGRAM,
                    checkbox=True))
        self.combo_fft.currentTextChanged.connect(
            partial(self.update,
                    "n_fft",
                    SoundPlayerSettings.GROUP_SPECTROGRAM))
        self.combo_scale.currentTextChanged.connect(
            partial(self.update,
                    "scale",
                    SoundPlayerSettings.GROUP_SPECTROGRAM))
        self.combo_window.currentTextChanged.connect(
            partial(self.update,
                    "window",
                    SoundPlayerSettings.GROUP_SPECTROGRAM))

        # Display
        self.cb_invert_colors.stateChanged.connect(
            partial(self.update,
                    "invert_colors",
                    SoundPlayerSettings.GROUP_IMAGE,
                    checkbox=True))
        self.spin_pix_in_sec.valueChanged.connect(
            partial(self.update,
                    "pixels_in_sec",
                    SoundPlayerSettings.GROUP_IMAGE))
        self.spin_height.valueChanged.connect(
            partial(self.update,
                    "height",
                    SoundPlayerSettings.GROUP_IMAGE))
        self.combo_color_map.currentTextChanged.connect(
            partial(self.update,
                    "color_map",
                    SoundPlayerSettings.GROUP_IMAGE))
        self.slider_contrast.valueChanged.connect(
            partial(self.update,
                    "contrast",
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

    def update(self, option, opt_group, value, checkbox=False):
        if checkbox:
            value = (value == QtCore.Qt.CheckState.Checked)
        self.options[opt_group][option] = value
        # emit signal to recompute image or spectrogram
        getattr(self, "update_" + opt_group).emit()

    def use_pcen(self, value):
        use_pcen = (value == QtCore.Qt.CheckState.Checked)
        self.cb_remove_noise.setEnabled(not use_pcen)
        self.update("pcen", SoundPlayerSettings.GROUP_SPECTROGRAM, use_pcen)

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
