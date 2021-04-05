#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to easily creator Range of Motion animations to easily test deformations
"""

from __future__ import print_function, division, absolute_import

import os
import sys

from tpDcc.core import tool

from tpRigToolkit.tools.romgenerator.core import consts, toolset, client


class RomGeneratorTool(tool.DccTool, object):

    ID = consts.TOOL_ID
    TOOLSET_CLASS = toolset.RomGeneratorToolset
    CLIENT_CLASS = client.RomGeneratorClient

    def __init__(self, *args, **kwargs):
        super(RomGeneratorTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = tool.DccTool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'ROM Generator',
            'id': cls.ID,
            'supported_dccs': {'maya': ['2017', '2018', '2019', '2020', '2022']},
            'icon': 'romgenerator',
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


if __name__ == '__main__':
    import tpRigToolkit.loader
    from tpDcc.managers import tools

    tool_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    if tool_path not in sys.path:
        sys.path.append(tool_path)

    tpRigToolkit.loader.init()

    tools.ToolsManager().launch_tool_by_id(consts.TOOL_ID)
