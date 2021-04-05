#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-romgenerator server implementation for Maya
"""

import maya.cmds

from tpDcc import dcc
from tpDcc.core import server


class RomGeneratorServer(server.DccServer, object):

    PORT = 45322

    def get_scene_joints(self, data, reply):
        long_joints = dcc.list_nodes(node_type='joint', full_path=True)
        short_joints = [dcc.node_short_name(joint) for joint in long_joints]
        joints_uuids = [dcc.node_handle(joint) for joint in long_joints]

        reply['result'] = {'names': short_joints, 'handles': joints_uuids}
        reply['success'] = True

    @dcc.undo_decorator()
    def generate_rom(self, data, reply):
        rom_data = data.get('rom_data', dict())
        if not rom_data:
            reply['success'] = False
            reply['msg'] = 'No ROM data given'
            return

        try:
            joint_handles = rom_data['joint_handles']
            rotate_x = rom_data['rotate_x']
            rotate_y = rom_data['rotate_y']
            rotate_z = rom_data['rotate_z']
            solve_as_one_item = rom_data['solve_as_one_item']
            frame_interval = rom_data['frame_interval']
            start_frame = rom_data['start_frame']
            anim_length = rom_data['anim_length']
        except Exception as exc:
            reply['success'] = False
            reply['msg'] = 'ROM data is not valid: {}'.format(exc)
            return

        # retrieve joints from UUIDs
        joints = [dcc.find_node_by_id(joint_id, full_path=True) for joint_id in joint_handles]
        joints = [joint for joint in joints if joint and dcc.node_exists(joint)]

        # set timeline and swipe existing keys
        dcc.set_active_frame_range(0, start_frame + anim_length)

        # swipe existing keys
        maya.cmds.cutKey(joints, time=(-100, anim_length * 10), option='keys')
        maya.cmds.setKeyframe(joints, t=start_frame)

        time = start_frame

        if solve_as_one_item:
            rotation_values = (0, 30, -30, 0)
            if rotate_x:
                for value in rotation_values:
                    maya.cmds.currentTime(time)
                    for joint in joints:
                        for axis in 'XYZ':
                            rotation_value = value if axis == 'X' else 0
                            dcc.set_attribute_value(joint, 'rotate{}'.format(axis), rotation_value)
                        maya.cmds.setKeyframe('{}.rotate'.format(joint))
                    time = time + frame_interval
            if rotate_y:
                for value in rotation_values:
                    maya.cmds.currentTime(time)
                    for joint in joints:
                        for axis in 'XYZ':
                            rotation_value = value if axis == 'Y' else 0
                            dcc.set_attribute_value(joint, 'rotate{}'.format(axis), rotation_value)
                        maya.cmds.setKeyframe('{}.rotate'.format(joint))
                    time = time + frame_interval
            if rotate_z:
                for value in rotation_values:
                    maya.cmds.currentTime(time)
                    for joint in joints:
                        for axis in 'XYZ':
                            rotation_value = value if axis == 'Z' else 0
                            dcc.set_attribute_value(joint, 'rotate{}'.format(axis), rotation_value)
                        maya.cmds.setKeyframe('{}.rotate'.format(joint))
                    time = time + frame_interval
        else:
            rotation_values = (0, 90, -90, 0)
            if rotate_x:
                for joint in joints:
                    for value in rotation_values:
                        maya.cmds.currentTime(time)
                        for axis in 'XYZ':
                            rotation_value = value if axis == 'X' else 0
                            dcc.set_attribute_value(joint, 'rotate{}'.format(axis), rotation_value)
                        maya.cmds.setKeyframe('{}.rotate'.format(joint))
                        time = time + frame_interval
            if rotate_y:
                for joint in joints:
                    for value in rotation_values:
                        maya.cmds.currentTime(time)
                        for axis in 'XYZ':
                            rotation_value = value if axis == 'Y' else 0
                            dcc.set_attribute_value(joint, 'rotate{}'.format(axis), rotation_value)
                        maya.cmds.setKeyframe('{}.rotate'.format(joint))
                        time = time + frame_interval
            if rotate_z:
                for joint in joints:
                    for value in rotation_values:
                        maya.cmds.currentTime(time)
                        for axis in 'XYZ':
                            rotation_value = value if axis == 'Z' else 0
                            dcc.set_attribute_value(joint, 'rotate{}'.format(axis), rotation_value)
                        maya.cmds.setKeyframe('{}.rotate'.format(joint))
                        time = time + frame_interval

        reply['success'] = True
