# -*- coding: utf-8 -*-
"""
"""

from __future__ import absolute_import, division, print_function


class Page(object):
    """Docstring for Page."""

    def __init__(self, items=None, count=None):
        self.items = items
        self.count = count

    def set_items(self, items):
        self.items = items

    def set_count(self, count):
        self.count = count

    def get_items(self):
        return self.items

    def get_count(self):
        return self.count

    def has_count(self):
        return self.count is not None
