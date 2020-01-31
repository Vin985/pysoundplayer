import functools
import itertools

import numpy as np
import webcolors
from PIL import Image, ImageEnhance, ImageOps
from ..common.options_object import OptionsObject


class ImageGenerator(OptionsObject):

    DEFAULT_OPTIONS = {"color_masks_str": ['red', 'lime', 'blue'],
                       "composite_ffts": [128, 512, 2048],
                       "contrast": 0,
                       "invert_colors": False}

    def __init__(self, image_options=None):
        super().__init__(options=image_options)
        self._color_masks = None

    def __getitem__(self, index):
        if index in self.options:
            return self.options[index]
        elif index in self.DEFAULT_OPTIONS:
            return self.DEFAULT_OPTIONS[index]
        raise KeyError(index + " option does not exist")

    @property
    def color_masks(self):
        if self._color_masks is None:
            self._color_masks = [self.__get_color_rgb(
                col) for col in self["color_masks_str"]]
        return self._color_masks

    def __get_color_rgb(self, color):
        if type(color) is tuple:
            return (color)
        elif type(color) is str:
            return (webcolors.name_to_rgb(color))

    # Prepare spectrograms to generate image
    def __prepare_spectrogram(self, spec):
        # Make sure spectrogram is in float32 because pillow doesn't
        # support float64
        spec = spec.astype("float32")
        # Normalize spectrogram in [0:1]
        # TODO: use librosa normalize?
        min = spec.min(axis=None)
        max = spec.max(axis=None)
        spec -= min
        spec /= (max - min)
        if self["invert_colors"]:
            spec = 1 - spec
        spec = spec * 255
        # flip upside down since writing image start from top left
        spec = np.flipud(spec)
        return spec

    def spec2img(self,
                 spec,
                 color_mask=(255, 0, 0),
                 size=None,
                 resize_method=Image.BILINEAR):

        spec = self.__prepare_spectrogram(spec)

        # Create image from float points
        img = Image.fromarray(spec, mode='F')
        # Convert in grayscale
        img = img.convert("L")
        # Colorise spectrogram
        if color_mask:
            img = ImageOps.colorize(img, (0, 0, 0), color_mask)

        # enhance contrast
        if self["contrast"]:
            if self["contrast"] == -1:
                img = ImageOps.autocontrast(img)
            else:
                c_enh = ImageEnhance.Contrast(img)
                img = c_enh.enhance(self["contrast"])

        if size is not None:
            img = img.resize(size, resize_method)

        return img

    def create_composite_part(self, spec, color_mask):
        img = self.spec2img(
            spec.spec, color_mask, size=(int(299 * spec.duration), 400))
        return np.asarray(img)

    def generate_composite(self, sample):
        # TODO: more checks
        if len(self["composite_ffts"]) != 3:
            print("3 spectrograms sizes must be provided in the "
                  " composite_ffts option in the configuration file")
            return ()
        specs = [
            sample.get_spectrogram({"n_fft": fft})
            for fft in self["composite_ffts"]
        ]
        res = itertools.starmap(self.create_composite_part,
                                zip(specs, self.color_masks))
        res = functools.reduce(np.add, res)
        composite = Image.fromarray(res, mode='RGB')
        return composite
