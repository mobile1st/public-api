from __future__ import absolute_import, division, print_function
from .models_map import modelsmap
from enum import Enum


def model_to_dict(obj):
    data = {}
    props = modelsmap[type(obj)]
    for prop in props:
        if isinstance(prop, tuple):
            prop, converter = prop
            if hasattr(obj, prop):
                data[prop] = converter(getattr(obj, prop))
        else:
            if hasattr(obj, prop):
                data[prop] = getattr(obj, prop)
    return data


def encode(obj):
    if type(obj) in modelsmap:
        return model_to_dict(obj), True
    if isinstance(obj, Enum):
        return obj.value, True
    return obj, False

