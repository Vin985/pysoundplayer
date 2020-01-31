class OptionsObject():

    DEFAULT_OPTIONS = {}

    def __init__(self, options):
        self.options = {} if options is None else options

    def __getitem__(self, index):
        if index in self.options:
            return self.options[index]
        elif index in self.DEFAULT_OPTIONS:
            return self.DEFAULT_OPTIONS[index]
        raise KeyError(index + " option does not exist")
