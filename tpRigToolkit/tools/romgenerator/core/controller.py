#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-romgenerator controller implementation
"""

from __future__ import print_function, division, absolute_import

import logging

from tpRigToolkit.tools.romgenerator.core import consts

logger = logging.getLogger(consts.TOOL_ID)


class RomGeneratorController(object):
    def __init__(self, model, client):
        super(RomGeneratorController, self).__init__()

        self._client = client
        self._model = model

    # =================================================================================================================
    # SETTERS
    # =================================================================================================================

    def set_rotate_x(self, flag):
        self._model.rotate_x = flag
        self.update_animation_length()

    def set_rotate_y(self, flag):
        self._model.rotate_y = flag
        self.update_animation_length()

    def set_rotate_z(self, flag):
        self._model.rotate_z = flag
        self.update_animation_length()

    def set_solve_as_one_item(self, flag):
        self._model.solve_as_one_item = flag
        self.update_animation_length()

    def set_interval_frames(self, value):
        self._model.interval_between_frames = value
        self.update_animation_length()

    def set_animation_start_frame(self, value):
        self._model.animation_start_frame = value
        self.update_animation_length()

    def set_selected_joints(self, joints_handles):
        self._model.selected_joints = joints_handles
        self.update_animation_length()

    # =================================================================================================================
    # BASE
    # =================================================================================================================

    def update_scene_joints(self):
        scene_joints = self._client.get_scene_joints() or dict()
        self._model.scene_joints = scene_joints

    def update_animation_length(self):
        anim_length = 0
        selected_joints = self._model.selected_joints
        if selected_joints:
            num_items = len(selected_joints)
            x_value = self._model.rotate_x
            y_value = self._model.rotate_y
            z_value = self._model.rotate_z
            group_solve = self._model.solve_as_one_item
            interval_frames = self._model.interval_between_frames
            multiplier = 0
            for flag in [x_value, y_value, z_value]:
                if flag:
                    multiplier += 1
            if group_solve:
                num_items = 1

            anim_length += (((multiplier * 4) * num_items) * interval_frames) - interval_frames

        self._model.animation_length = anim_length

    def generate_rom(self):
        rom_data = {
            'joint_handles': self._model.selected_joints,
            'rotate_x': self._model.rotate_x,
            'rotate_y': self._model.rotate_y,
            'rotate_z': self._model.rotate_z,
            'solve_as_one_item': self._model.solve_as_one_item,
            'frame_interval': self._model.interval_between_frames,
            'start_frame': self._model.animation_start_frame,
            'anim_length': self._model.animation_length
        }

        if not rom_data['joint_handles']:
            logger.warning('At least one joint from the list must be selected!')
            return False

        return self._client.generate_rom(rom_data)

    def clear_rom(self):
        joint_handles = self._model.selected_joints
        if not joint_handles:
            return False

        return self._client.clear_rom(joint_handles)
