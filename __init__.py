from Item import *
import json


def export(items):
    obj = {"items": [item.value for item in items]}
    print(json.dumps(obj))