import mlbv.mlbam.common.config as config


LOG = None


class ANSI(object):
    CONTROL_CODE = {
        "reset": "[0m",
        "bold": "[01m",
        "disable": "[02m",
        "underline": "[04m",
        "reverse": "[07m",
        "strikethrough": "[09m",
        "invisible": "[08m",
    }
    FG_COLOUR = {
        "black": "[30m",
        "red": "[31m",
        "green": "[32m",
        "orange": "[33m",
        "blue": "[34m",
        "purple": "[35m",
        "cyan": "[36m",
        "lightgrey": "[37m",
        "darkgrey": "[90m",
        "lightred": "[91m",
        "lightgreen": "[92m",
        "yellow": "[93m",
        "lightblue": "[94m",
        "pink": "[95m",
        "lightcyan": "[96m",
    }
    BG_COLOUR = {
        "black": "[40m",
        "red": "[41m",
        "green": "[42m",
        "orange": "[43m",
        "blue": "[44m",
        "purple": "[45m",
        "cyan": "[46m",
        "lightgrey": "[47m",
    }

    @staticmethod
    def control_code(code):
        if code is not None and code != "" and code in ANSI.CONTROL_CODE:
            return ANSI.CONTROL_CODE[code]
        # raise AttributeError('Unknown colour: ' + colour_name)
        return ""

    @staticmethod
    def reset():
        return ANSI.CONTROL_CODE["reset"]

    @staticmethod
    def fg(colour_name):
        if (
            colour_name is not None
            and colour_name != ""
            and colour_name in ANSI.FG_COLOUR
        ):
            return ANSI.FG_COLOUR[colour_name]
        # raise AttributeError('Unknown colour: ' + colour_name)
        return ""

    @staticmethod
    def bg(colour_name):
        if (
            colour_name is not None
            and colour_name != ""
            and colour_name in ANSI.BG_COLOUR
        ):
            return ANSI.FG_COLOUR[colour_name]
        # raise AttributeError('Unknown colour: ' + colour_name)
        return ""


class Border(object):
    """Holds border symbols.
    Some unicode characters:  '─' '┄' '╌' '═' '━' '─'
    """

    def __init__(self, use_unicode=True):
        if use_unicode:
            # unicode characters:  '─' '┄' '╌' '═' '━' '─'
            self.border_color = ANSI.fg("darkgrey")
            self.color_off = ANSI.reset()
            self.dash = "─"
            self.thickdash = "─"
            self.doubledash = "═"
            self.pipe = self.border_color + "│" + self.color_off
            self.junction = "┼"
        else:
            # unicode characters:  '─' '┄' '╌' '═' '━' '─'
            self.border_color = ANSI.fg("darkgrey")
            self.color_off = ANSI.reset()
            self.dash = "-"
            self.thickdash = "-"
            self.doubledash = "="
            self.pipe = self.border_color + "|" + self.color_off
            self.junction = "|"
