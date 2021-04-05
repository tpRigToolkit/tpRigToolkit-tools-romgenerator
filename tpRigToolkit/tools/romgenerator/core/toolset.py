#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains toolset implementation for tpRigToolkit-tools-romgenerator
"""

from __future__ import print_function, division, absolute_import

from tpDcc.libs.qt.widgets import toolset


class RomGeneratorToolset(toolset.ToolsetWidget, object):
    def __init__(self, *args, **kwargs):
        super(RomGeneratorToolset, self).__init__(*args, **kwargs)

    def contents(self):
        return []
