#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to easily creator Range of Motion animations to easily test deformations
"""

from __future__ import print_function, division, absolute_import

from tpDcc.core import tool
from tpDcc.libs.qt.widgets import toolset

# Defines ID of the tool
TOOL_ID = 'tpRigToolkit-tools-romgenerator'


class RomGeneratorTool(tool.DccTool, object):
    def __init__(self, *args, **kwargs):
        super(RomGeneratorTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = tool.DccTool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'ROM Generator',
            'id': TOOL_ID,
            'supported_dccs': {'maya': ['2017', '2018', '2019', '2020', '2022']},
            'icon': 'rom',
            'tooltip': 'Tool to easily creator Range of Motion animations to easily test deformations',
            'tags': ['tpRigToolkit', 'dcc', 'tool', 'rom', 'deformation', 'generator'],
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'ROM Generator', 'load_on_startup': False, 'color': '', 'background_color': ''},
        }
        base_tool_config.update(tool_config)

        return base_tool_config

    def launch(self, *args, **kwargs):
        return self.launch_frameless(*args, **kwargs)


class RomGeneratorToolset(toolset.ToolsetWidget, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(RomGeneratorToolset, self).__init__(*args, **kwargs)

    def contents(self):
        return []
