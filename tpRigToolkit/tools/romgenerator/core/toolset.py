#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains toolset implementation for tpRigToolkit-tools-romgenerator
"""

from __future__ import print_function, division, absolute_import

from tpDcc.libs.qt.widgets import toolset

from tpRigToolkit.tools.romgenerator.core import model, view, controller


class RomGeneratorToolset(toolset.ToolsetWidget, object):
    def __init__(self, *args, **kwargs):
        super(RomGeneratorToolset, self).__init__(*args, **kwargs)

    def contents(self):
        rom_model = model.RomGeneratorModel()
        rom_controller = controller.RomGeneratorController(model=rom_model, client=self.client)
        rom_view = view.RomGeneratorView(model=rom_model, controller=rom_controller, parent=self)

        return [rom_view]
