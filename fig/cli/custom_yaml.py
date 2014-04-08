import os.path
import yaml

# Stolen from Stackoverflow:
# http://stackoverflow.com/questions/528281/how-can-i-include-an-yaml-file-inside-another
root = os.path.curdir


def include(loader, node):
    """Include another YAML file."""

    global root

    old_root = root

    filename = os.path.join(root, loader.construct_scalar(node))
    root = os.path.split(filename)[0]

    data = yaml.load(open(filename, 'r'))

    root = old_root

    return data

yaml.add_constructor(u'!include', include)