# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)

"""
Spyder appearance configuration
"""

import os
import sys

from spyder.config.fonts import MEDIUM, MONOSPACE, SANS_SERIF, SMALL

WIN = os.name == 'nt'
LINUX = sys.platform.startswith('linux')

# Default themes
APPEARANCE = {
    'icon_theme': 'spyder 3',
    # Global Spyder fonts
    'font/family': MONOSPACE,
    'font/size': MEDIUM,
    'font/italic': False,
    'font/bold': False,
    'rich_font/family': SANS_SERIF,
    'rich_font/size': SMALL if (LINUX or WIN) else MEDIUM,
    'rich_font/italic': False,
    'rich_font/bold': False,
    'ui_theme': 'automatic',
    'names': ['emacs', 'idle', 'monokai', 'pydev', 'scintilla',
              'spyder', 'spyder/dark', 'zenburn', 'solarized/light',
              'solarized/dark', 'inkpot', 'minimal', 'nightlion',
              'notepad++', 'oblivion', 'obsidian', 'pastel', 'retta',
              'roboticket', 'sublime-monokai/extended', 'vibrant-ink'],
    'selected': 'spyder',
    # ---- Emacs ----
    'emacs/name':        "Emacs",
    #      Name            Color     Bold  Italic
    'emacs/background':  "#000000",
    'emacs/currentline': "#2b2b43",
    'emacs/currentcell': "#1c1c2d",
    'emacs/occurrence':   "#abab67",
    'emacs/ctrlclick':   "#0000ff",
    'emacs/sideareas':   "#555555",
    'emacs/matched_p':   "#009800",
    'emacs/unmatched_p': "#c80000",
    'emacs/normal':     ('#ffffff', False, False),
    'emacs/keyword':    ('#3c51e8', False, False),
    'emacs/builtin':    ('#900090', False, False),
    'emacs/definition': ('#ff8040', True, False),
    'emacs/comment':    ('#005100', False, False),
    'emacs/string':     ('#00aa00', False, True),
    'emacs/number':     ('#800000', False, False),
    'emacs/instance':   ('#ffffff', False, True),
    # ---- IDLE ----
    'idle/name':         "IDLE",
    #      Name            Color     Bold  Italic
    'idle/background':   "#ffffff",
    'idle/currentline':  "#f2e6f3",
    'idle/currentcell':  "#feefff",
    'idle/occurrence':    "#e8f2fe",
    'idle/ctrlclick':    "#0000ff",
    'idle/sideareas':    "#efefef",
    'idle/matched_p':    "#99ff99",
    'idle/unmatched_p':  "#ff9999",
    'idle/normal':      ('#000000', False, False),
    'idle/keyword':     ('#ff7700', True, False),
    'idle/builtin':     ('#900090', False, False),
    'idle/definition':  ('#0000ff', False, False),
    'idle/comment':     ('#dd0000', False, True),
    'idle/string':      ('#00aa00', False, False),
    'idle/number':      ('#924900', False, False),
    'idle/instance':    ('#777777', True, True),
    # ---- Monokai ----
    'monokai/name':         "Monokai",
    #      Name              Color     Bold  Italic
    'monokai/background':   "#2a2b24",
    'monokai/currentline':  "#484848",
    'monokai/currentcell':  "#3d3d3d",
    'monokai/occurrence':    "#666666",
    'monokai/ctrlclick':    "#0000ff",
    'monokai/sideareas':    "#2a2b24",
    'monokai/matched_p':    "#688060",
    'monokai/unmatched_p':  "#bd6e76",
    'monokai/normal':      ("#ddddda", False, False),
    'monokai/keyword':     ("#f92672", False, False),
    'monokai/builtin':     ("#ae81ff", False, False),
    'monokai/definition':  ("#a6e22e", False, False),
    'monokai/comment':     ("#75715e", False, True),
    'monokai/string':      ("#e6db74", False, False),
    'monokai/number':      ("#ae81ff", False, False),
    'monokai/instance':    ("#ddddda", False, True),
    # ---- Pydev ----
    'pydev/name':        "Pydev",
    #      Name            Color     Bold  Italic
    'pydev/background':  "#ffffff",
    'pydev/currentline': "#e8f2fe",
    'pydev/currentcell': "#eff8fe",
    'pydev/occurrence':   "#ffff99",
    'pydev/ctrlclick':   "#0000ff",
    'pydev/sideareas':   "#efefef",
    'pydev/matched_p':   "#99ff99",
    'pydev/unmatched_p': "#ff99992",
    'pydev/normal':     ('#000000', False, False),
    'pydev/keyword':    ('#0000ff', False, False),
    'pydev/builtin':    ('#900090', False, False),
    'pydev/definition': ('#000000', True, False),
    'pydev/comment':    ('#c0c0c0', False, False),
    'pydev/string':     ('#00aa00', False, True),
    'pydev/number':     ('#800000', False, False),
    'pydev/instance':   ('#000000', False, True),
    # ---- Scintilla ----
    'scintilla/name':        "Scintilla",
    #         Name             Color     Bold  Italic
    'scintilla/background':  "#ffffff",
    'scintilla/currentline': "#e1f0d1",
    'scintilla/currentcell': "#edfcdc",
    'scintilla/occurrence':   "#ffff99",
    'scintilla/ctrlclick':   "#0000ff",
    'scintilla/sideareas':   "#efefef",
    'scintilla/matched_p':   "#99ff99",
    'scintilla/unmatched_p': "#ff9999",
    'scintilla/normal':     ('#000000', False, False),
    'scintilla/keyword':    ('#00007f', True, False),
    'scintilla/builtin':    ('#000000', False, False),
    'scintilla/definition': ('#007f7f', True, False),
    'scintilla/comment':    ('#007f00', False, False),
    'scintilla/string':     ('#7f007f', False, False),
    'scintilla/number':     ('#007f7f', False, False),
    'scintilla/instance':   ('#000000', False, True),
    # ---- Spyder ----
    'spyder/name':        "Spyder",
    #       Name            Color     Bold  Italic
    'spyder/background':  "#ffffff",
    'spyder/currentline': "#f7ecf8",
    'spyder/currentcell': "#fdfdde",
    'spyder/occurrence':   "#ffff99",
    'spyder/ctrlclick':   "#0000ff",
    'spyder/sideareas':   "#efefef",
    'spyder/matched_p':   "#99ff99",
    'spyder/unmatched_p': "#ff9999",
    'spyder/normal':     ('#000000', False, False),
    'spyder/keyword':    ('#0000ff', False, False),
    'spyder/builtin':    ('#900090', False, False),
    'spyder/definition': ('#000000', True, False),
    'spyder/comment':    ('#adadad', False, True),
    'spyder/string':     ('#00aa00', False, False),
    'spyder/number':     ('#800000', False, False),
    'spyder/instance':   ('#924900', False, True),
    # ---- Spyder/Dark ----
    'spyder/dark/name':        "Spyder Dark",
    #           Name             Color     Bold  Italic
    'spyder/dark/background':  "#19232D",
    'spyder/dark/currentline': "#3a424a",
    'spyder/dark/currentcell': "#292d3e",
    'spyder/dark/occurrence':  "#509ea5",
    'spyder/dark/ctrlclick':   "#179ae0",
    'spyder/dark/sideareas':   "#222b35",
    'spyder/dark/matched_p':   "#0bbe0b",
    'spyder/dark/unmatched_p': "#ff4340",
    'spyder/dark/normal':     ('#ffffff', False, False),
    'spyder/dark/keyword':    ('#c670e0', False, False),
    'spyder/dark/builtin':    ('#fab16c', False, False),
    'spyder/dark/definition': ('#57d6e4', True, False),
    'spyder/dark/comment':    ('#999999', False, False),
    'spyder/dark/string':     ('#b0e686', False, True),
    'spyder/dark/number':     ('#faed5c', False, False),
    'spyder/dark/instance':   ('#ee6772', False, True),
    # ---- Zenburn ----
    'zenburn/name':        "Zenburn",
    #        Name            Color     Bold  Italic
    'zenburn/background':  "#3f3f3f",
    'zenburn/currentline': "#333333",
    'zenburn/currentcell': "#2c2c2c",
    'zenburn/occurrence':   "#7a738f",
    'zenburn/ctrlclick':   "#0000ff",
    'zenburn/sideareas':   "#3f3f3f",
    'zenburn/matched_p':   "#688060",
    'zenburn/unmatched_p': "#bd6e76",
    'zenburn/normal':     ('#dcdccc', False, False),
    'zenburn/keyword':    ('#dfaf8f', True, False),
    'zenburn/builtin':    ('#efef8f', False, False),
    'zenburn/definition': ('#efef8f', False, False),
    'zenburn/comment':    ('#7f9f7f', False, True),
    'zenburn/string':     ('#cc9393', False, False),
    'zenburn/number':     ('#8cd0d3', False, False),
    'zenburn/instance':   ('#dcdccc', False, True),
    # ---- Solarized Light ----
    'solarized/light/name':        "Solarized Light",
    #        Name            Color     Bold  Italic
    'solarized/light/background':  '#fdf6e3',
    'solarized/light/currentline': '#f5efdB',
    'solarized/light/currentcell': '#eee8d5',
    'solarized/light/occurrence':   '#839496',
    'solarized/light/ctrlclick':   '#d33682',
    'solarized/light/sideareas':   '#eee8d5',
    'solarized/light/matched_p':   '#586e75',
    'solarized/light/unmatched_p': '#dc322f',
    'solarized/light/normal':     ('#657b83', False, False),
    'solarized/light/keyword':    ('#859900', False, False),
    'solarized/light/builtin':    ('#6c71c4', False, False),
    'solarized/light/definition': ('#268bd2', True, False),
    'solarized/light/comment':    ('#93a1a1', False, True),
    'solarized/light/string':     ('#2aa198', False, False),
    'solarized/light/number':     ('#cb4b16', False, False),
    'solarized/light/instance':   ('#b58900', False, True),
    # ---- Solarized Dark ----
    'solarized/dark/name':        "Solarized Dark",
    #        Name            Color     Bold  Italic
    'solarized/dark/background':  '#002b36',
    'solarized/dark/currentline': '#083f4d',
    'solarized/dark/currentcell': '#073642',
    'solarized/dark/occurrence':  '#657b83',
    'solarized/dark/ctrlclick':   '#d33682',
    'solarized/dark/sideareas':   '#073642',
    'solarized/dark/matched_p':   '#93a1a1',
    'solarized/dark/unmatched_p': '#dc322f',
    'solarized/dark/normal':     ('#839496', False, False),
    'solarized/dark/keyword':    ('#859900', False, False),
    'solarized/dark/builtin':    ('#6c71c4', False, False),
    'solarized/dark/definition': ('#268bd2', True, False),
    'solarized/dark/comment':    ('#586e75', False, True),
    'solarized/dark/string':     ('#2aa198', False, False),
    'solarized/dark/number':     ('#cb4b16', False, False),
    'solarized/dark/instance':   ('#b58900', False, True),
    # ---- Inkpot (Eclipse color theme) ----
    'inkpot/name':        "Inkpot",
    #      Name             Color     Bold  Italic
    'inkpot/background':  "#1f1f27",
    'inkpot/currentline': "#2d2d44",
    'inkpot/currentcell': "#33333A",
    'inkpot/occurrence':  "#616161",
    'inkpot/ctrlclick':   "#1f1f27",
    'inkpot/sideareas':   "#2d2d44",
    'inkpot/matched_p':   "#cfbfad",
    'inkpot/unmatched_p': "#8b8bff",
    'inkpot/normal':     ('#cfbfad', False, False),
    'inkpot/keyword':    ('#808bed', False, False),
    'inkpot/builtin':    ('#87cefa', False, False),
    'inkpot/definition': ('#87cefa', False, False),
    'inkpot/comment':    ('#cd8b00', False, False),
    'inkpot/string':     ('#ffcd8b', False, False),
    'inkpot/number':     ('#ffcd8b', False, False),
    'inkpot/instance':   ('#cfbfad', False, False),
    # ---- minimal (Eclipse color theme) ----
    'minimal/name':        "Minimal",
    #      Name              Color     Bold  Italic
    'minimal/background':  "#ffffff",
    'minimal/currentline': "#aaccff",
    'minimal/currentcell': "#E7F1FF",
    'minimal/occurrence':  "#efefef",
    'minimal/ctrlclick':   "#05314d",
    'minimal/sideareas':   "#aaccff",
    'minimal/matched_p':   "#000000",
    'minimal/unmatched_p': "#efefff",
    'minimal/normal':     ('#000000', False, False),
    'minimal/keyword':    ('#5c8198', False, False),
    'minimal/builtin':    ('#000066', False, False),
    'minimal/definition': ('#5c8198', False, False),
    'minimal/comment':    ('#334466', False, False),
    'minimal/string':     ('#333333', False, False),
    'minimal/number':     ('#333333', False, False),
    'minimal/instance':   ('#566874', False, False),
    # ---- NightLion Aptana Theme (Eclipse color theme) ----
    'nightlion/name':        "NightLion Aptana Theme",
    #      Name                             Color     Bold  Italic
    'nightlion/background':  "#1e1e1e",
    'nightlion/currentline': "#505050",
    'nightlion/currentcell': "#323232",
    'nightlion/occurrence':  "#616161",
    'nightlion/ctrlclick':   "#b3b5af",
    'nightlion/sideareas':   "#505050",
    'nightlion/matched_p':   "#e2e2e2",
    'nightlion/unmatched_p': "#364656",
    'nightlion/normal':     ('#e2e2e2', False, False),
    'nightlion/keyword':    ('#8dcbe2', False, False),
    'nightlion/builtin':    ('#cae682', False, False),
    'nightlion/definition': ('#dfbe95', False, False),
    'nightlion/comment':    ('#7f9f7f', False, False),
    'nightlion/string':     ('#cc9393', False, False),
    'nightlion/number':     ('#eab882', False, False),
    'nightlion/instance':   ('#b3b784', False, False),
    # ---- Notepad++ (Eclipse color theme) ----
    'notepad++/name':        "Notepad++",
    #      Name                     Color     Bold  Italic
    'notepad++/background':  "#ffffff",
    'notepad++/currentline': "#eeeeee",
    'notepad++/currentcell': "#D9D9D9",
    'notepad++/occurrence':  "#efefef",
    'notepad++/ctrlclick':   "#800080",
    'notepad++/sideareas':   "#eeeeee",
    'notepad++/matched_p':   "#8000ff",
    'notepad++/unmatched_p': "#eeeeee",
    'notepad++/normal':     ('#8000ff', False, False),
    'notepad++/keyword':    ('#0000ff', False, False),
    'notepad++/builtin':    ('#000080', False, False),
    'notepad++/definition': ('#ff00ff', False, False),
    'notepad++/comment':    ('#008000', False, False),
    'notepad++/string':     ('#808080', False, False),
    'notepad++/number':     ('#ff8000', False, False),
    'notepad++/instance':   ('#800080', False, False),
    # ---- Oblivion (Eclipse color theme) ----
    'oblivion/name':        "Oblivion",
    #      Name               Color     Bold  Italic
    'oblivion/background':  "#1e1e1e",
    'oblivion/currentline': "#2a2a2a",
    'oblivion/currentcell': "#323232",
    'oblivion/occurrence':  "#000000",
    'oblivion/ctrlclick':   "#ccdf32",
    'oblivion/sideareas':   "#2a2a2a",
    'oblivion/matched_p':   "#d8d8d8",
    'oblivion/unmatched_p': "#000000",
    'oblivion/normal':     ('#d8d8d8', False, False),
    'oblivion/keyword':    ('#ffffff', False, False),
    'oblivion/builtin':    ('#d25252', False, False),
    'oblivion/definition': ('#ffffff', False, False),
    'oblivion/comment':    ('#c7dd0c', False, False),
    'oblivion/string':     ('#ffc600', False, False),
    'oblivion/number':     ('#7fb347', False, False),
    'oblivion/instance':   ('#bed6ff', False, False),
    # ---- Obsidian (Eclipse color theme) ----
    'obsidian/name':        "Obsidian",
    #      Name               Color     Bold  Italic
    'obsidian/background':  "#293134",
    'obsidian/currentline': "#2f393c",
    'obsidian/currentcell': "#3C4346",
    'obsidian/occurrence':  "#616161",
    'obsidian/ctrlclick':   "#7d8c93",
    'obsidian/sideareas':   "#2f393c",
    'obsidian/matched_p':   "#e0e2e4",
    'obsidian/unmatched_p': "#804000",
    'obsidian/normal':     ('#e0e2e4', False, False),
    'obsidian/keyword':    ('#93c763', False, False),
    'obsidian/builtin':    ('#678cb1', False, False),
    'obsidian/definition': ('#678cb1', False, False),
    'obsidian/comment':    ('#7d8c93', False, False),
    'obsidian/string':     ('#ec7600', False, False),
    'obsidian/number':     ('#ffcd22', False, False),
    'obsidian/instance':   ('#678cb1', False, False),
    # ---- Pastel (Eclipse color theme) ----
    'pastel/name':        "Pastel",
    #      Name             Color     Bold  Italic
    'pastel/background':  "#1f2223",
    'pastel/currentline': "#2f393c",
    'pastel/currentcell': "#454849",
    'pastel/occurrence':  "#616161",
    'pastel/ctrlclick':   "#7d8c93",
    'pastel/sideareas':   "#2f393c",
    'pastel/matched_p':   "#e0e2e4",
    'pastel/unmatched_p': "#95bed8",
    'pastel/normal':     ('#e0e2e4', False, False),
    'pastel/keyword':    ('#a57b61', False, False),
    'pastel/builtin':    ('#678cb1', False, False),
    'pastel/definition': ('#678cb1', False, False),
    'pastel/comment':    ('#7d8c93', False, False),
    'pastel/string':     ('#c78d9b', False, False),
    'pastel/number':     ('#c78d9b', False, False),
    'pastel/instance':   ('#678cb1', False, False),
    # ---- Retta (Eclipse color theme) ----
    'retta/name':        "Retta",
    #      Name            Color     Bold  Italic
    'retta/background':  "#000000",
    'retta/currentline': "#2a2a2a",
    'retta/currentcell': "#171717",
    'retta/occurrence':  "#5e5c56",
    'retta/ctrlclick':   "#83786e",
    'retta/sideareas':   "#2a2a2a",
    'retta/matched_p':   "#f8e1aa",
    'retta/unmatched_p': "#527d5d",
    'retta/normal':     ('#f8e1aa', False, False),
    'retta/keyword':    ('#e79e3c', True, False),
    'retta/builtin':    ('#de6546', True, False),
    'retta/definition': ('#a4b0c0', False, False),
    'retta/comment':    ('#83786e', False, False),
    'retta/string':     ('#d6c248', False, False),
    'retta/number':     ('#d6c248', False, False),
    'retta/instance':   ('#de6546', False, False),
    # ---- Roboticket (Eclipse color theme) ----
    'roboticket/name':        "Roboticket",
    #      Name                 Color     Bold  Italic
    'roboticket/background':  "#f5f5f5",
    'roboticket/currentline': "#e0e0ff",
    'roboticket/currentcell': "#CCCCE8",
    'roboticket/occurrence':  "#ffcfbb",
    'roboticket/ctrlclick':   "#ad95af",
    'roboticket/sideareas':   "#e0e0ff",
    'roboticket/matched_p':   "#585858",
    'roboticket/unmatched_p': "#bdd8f2",
    'roboticket/normal':     ('#585858', False, False),
    'roboticket/keyword':    ('#295f94', False, True),
    'roboticket/builtin':    ('#ab2525', False, False),
    'roboticket/definition': ('#bc5a65', True, False),
    'roboticket/comment':    ('#ad95af', False, True),
    'roboticket/string':     ('#317ecc', False, False),
    'roboticket/number':     ('#af0f91', False, False),
    'roboticket/instance':   ('#566874', False, False),
    # ---- Sublime Text Monokai Extended (Eclipse color theme) ----
    'sublime-monokai/extended/name':        "Sublime Text Monokai Extended",
    #      Name                       Color     Bold  Italic
    'sublime-monokai/extended/background':  "#222222",
    'sublime-monokai/extended/currentline': "#2f2f2f",
    'sublime-monokai/extended/currentcell': "#363636",
    'sublime-monokai/extended/occurrence':  "#000000",
    'sublime-monokai/extended/ctrlclick':   "#ffffff",
    'sublime-monokai/extended/sideareas':   "#2f2f2f",
    'sublime-monokai/extended/matched_p':   "#cfbfad",
    'sublime-monokai/extended/unmatched_p': "#cc9900",
    'sublime-monokai/extended/normal':     ('#cfbfad', False, False),
    'sublime-monokai/extended/keyword':    ('#ff007f', False, False),
    'sublime-monokai/extended/builtin':    ('#52e3f6', False, False),
    'sublime-monokai/extended/definition': ('#a7ec21', False, False),
    'sublime-monokai/extended/comment':    ('#ffffff', False, False),
    'sublime-monokai/extended/string':     ('#ece47e', False, False),
    'sublime-monokai/extended/number':     ('#c48cff', False, False),
    'sublime-monokai/extended/instance':   ('#cfbfad', False, False),
    # ---- Vibrant Ink (Eclipse color theme) ----
    'vibrant-ink/name':        "Vibrant Ink",
    #      Name                  Color     Bold  Italic
    'vibrant-ink/background':  "#191919",
    'vibrant-ink/currentline': "#222220",
    'vibrant-ink/currentcell': "#2D2D2D",
    'vibrant-ink/occurrence':  "#616161",
    'vibrant-ink/ctrlclick':   "#8c3fc8",
    'vibrant-ink/sideareas':   "#222220",
    'vibrant-ink/matched_p':   "#ffffff",
    'vibrant-ink/unmatched_p': "#414c3b",
    'vibrant-ink/normal':     ('#ffffff', False, False),
    'vibrant-ink/keyword':    ('#ec691e', False, False),
    'vibrant-ink/builtin':    ('#9cf828', False, False),
    'vibrant-ink/definition': ('#f7c527', False, False),
    'vibrant-ink/comment':    ('#8146a2', False, False),
    'vibrant-ink/string':     ('#477488', False, False),
    'vibrant-ink/number':     ('#477488', False, False),
    'vibrant-ink/instance':   ('#357a8f', False, False)
}
