"""
https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
"""

from enum import Enum
import json


class Item:
    class Type(Enum):
        DEFAULT = "default"
        FILE = "file"
        SKIPCHECK = "file:skipcheck"

    def __init__(self, title, subtitle, icon, arg=None,
                 valid=True, match=None, autocomplete=None,
                 type=None, mods=None, text=None, quicklookurl=None):
        self.title = title
        self.subtitle = subtitle
        self.icon = icon
        self.arg = arg
        self.valid = valid
        self.match = match
        self.autocomplete = autocomplete
        self.type = type
        self.mods = mods
        self.text = text
        self.quicklookurl = quicklookurl

    @property
    def value(self):
        obj = self.__dict__.copy()
        none_keys = [key for key in obj if obj[key] == None]
        for key in none_keys:
            del obj[key]
        obj["icon"] = self.icon.value
        if "type" in obj:
            obj["type"] = self.type.value
        if "mods" in obj:
            obj["mods"] = {}
            for mod in self.mods:
                obj["mods"].update(mod.value)
        if "text" in obj:
            obj["text"] = {}
            for t in self.text:
                obj["text"].update(t.value)
        return obj

class Icon:
    class Type(Enum):
        FILEICON = "fileicon"
        FILEPATH = "filepath"

    def __init__(self, path, type=None):
        self.path = path
        if type is not None:
            self.type = type

    @property
    def value(self):
        obj = self.__dict__.copy()
        if "type" in obj:
            obj["type"] = self.type.value
        return obj


class Mod:
    class Type(Enum):
        ALT = "alt"
        CMD = "cmd"
        CTRL = "ctrl"

    def __init__(self, subtitle, arg, type, valid=True):
        self.subtitle = subtitle
        self.arg = arg
        self.type = type
        self.valid = valid

    @property
    def value(self):
        obj = self.__dict__.copy()
        del obj["type"]
        return {self.type.value: obj}


class Text:
    class Type(Enum):
        COPY = "copy"
        LARGETYPE = "largetype"

    def __init__(self, text, type):
        self.text = text
        self.type = type

    @property
    def value(self):
        return {self.type.value: self.text}

