import ast
import logging

from PySide2.QtCore import QSettings
from ..spectrogram.spectrogram import Spectrogram
from ..spectrogram.image import ImageGenerator


class SoundPlayerSettings(QSettings):

    GROUP_SPECTROGRAM = "spectrogram"
    GROUP_IMAGE = "image"

    def __init__(self):
        super().__init__()
        self.default_options = {self.GROUP_SPECTROGRAM: Spectrogram.DEFAULT_OPTIONS,
                                self.GROUP_IMAGE: ImageGenerator.DEFAULT_OPTIONS}
        self.options = {self.GROUP_SPECTROGRAM: self.spectrogram_settings(
        ), self.GROUP_IMAGE: self.image_settings()}
        self.all_settings()
        self.save_group(self.GROUP_SPECTROGRAM, self.options["spectrogram"])
        self.save_group(self.GROUP_IMAGE, self.options[self.GROUP_IMAGE])

    def all_settings(self):
        print("loading all keys")
        res = {}
        for key in self.allKeys():
            res[key] = self.value(key)
        print(res)

    @property
    def spectrogram_options(self):
        return self.options[self.GROUP_SPECTROGRAM]

    @property
    def image_options(self):
        return self.options[self.GROUP_IMAGE]

    def get(self, key, group=None):
        default = repr(self.default_options[group][key])
        tmp = self.value(key, default)
        if tmp is None:
            return tmp
        return ast.literal_eval(tmp)

    def save(self, key, value):
        self.setValue(key, value)
        self.sync()

    def save_group(self, group_name, values):
        self.beginGroup(group_name)
        for key, value in values.items():
            self.save(key, value)
        self.endGroup()
        self.sync()

    def setValue(self, key, value):
        valrepr = repr(value)
        try:
            assert value == ast.literal_eval(valrepr)
        except (ValueError, AssertionError, SyntaxError):
            raise ValueError(('Value too complex to store.'
                              ' Can only store values for which x == ast.literal_eval(repr(x))'))
        super().setValue(key, valrepr)

    def group_to_dict(self, group=""):
        opts = {}
        self.beginGroup(group)
        for key in self.childKeys():
            if key.startswith("__"):
                continue
            opts[key] = self.get(key, group)
        self.endGroup()
        return opts

    def get_spec_setting(self, key):
        return self.get(key, self.GROUP_SPECTROGRAM)

    def get_image_setting(self, key):
        return self.get(key, self.GROUP_IMAGE)

    def spectrogram_settings(self, context=""):
        group = self.GROUP_SPECTROGRAM
        res = {}
        # Spectrogram settings
        if context:
            context = "/" + context
        self.beginGroup(group + context)
        if context and not self.childKeys():
            logging.info(
                "No entries found for selected context, using default group")
            self.endGroup()
            self.beginGroup(group)
        for key in self.childKeys():
            res[key] = self.get_spec_setting(key)
        # res["window"] = self.get_spec_setting("window")
        # res["n_fft"] = self.get_spec_setting("n_fft")
        # res["pcen"] = self.get_spec_setting("pcen")
        # res["to_db"] = self.get_spec_setting("to_db")
        # res["normalize"] = self.get_spec_setting("normalize")
        # res["hop_length"] = self.get_spec_setting("hop_length")
        # res["scale"] = self.get_spec_setting("scale")
        # res["remove_noise"] = self.get_spec_setting("remove_noise")
        # res["nr_hist_rel_size"] = self.get_spec_setting("nr_hist_rel_size")
        # res["nr_N"] = self.get_spec_setting("nr_N")
        # res["nr_window_smoothing"] = self.get_spec_setting(
        #     "nr_window_smoothing")
        self.endGroup()
        return res

    # TODO: Automatize value loading based on childkeys

    def image_settings(self):
        res = {}
        self.beginGroup(self.GROUP_IMAGE)
        # res["color_masks_str"] = self.get_image_setting(
        #     "color_masks_str")
        # res["contrast"] = self.get_image_setting("contrast")
        # res["invert_colors"] = self.get_image_setting("invert_colors")
        # res["composite_ffts"] = self.get_image_setting("composite_ffts")
        # res["height"] = self.get_image_setting("height")
        # res["pixels_in_sec"] = self.get_image_setting("pixels_in_sec")
        # res["color_map"] = self.get_image_setting("color_map")
        for key in self.childKeys():
                res[key] = self.get_image_setting(key)
        # res["composite_ffts"] = [int(i) for i in composite_ffts]
        self.endGroup()
        return res
