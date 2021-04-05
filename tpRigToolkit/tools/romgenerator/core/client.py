#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-romgenerator client implementation
"""

from tpDcc.core import client


class RomGeneratorClient(client.DccClient, object):

    PORT = 45322

    # =================================================================================================================
    # BASE
    # =================================================================================================================

    def get_scene_joints(self):
        cmd = {
            'cmd': 'get_scene_joints'
        }

        reply_dict = self.send(cmd)

        if not self.is_valid_reply(reply_dict):
            return False

        return reply_dict['result']

    def generate_rom(self, rom_data):
        cmd = {
            'cmd': 'generate_rom',
            'rom_data': rom_data
        }

        reply_dict = self.send(cmd)

        if not self.is_valid_reply(reply_dict):
            return False

        return reply_dict['result']
