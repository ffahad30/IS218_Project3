"""Absolute path"""
from pathlib import Path


def absolutepath(filepath):
    """ absolute path"""
    relative = Path(filepath)
    return relative.absolute()