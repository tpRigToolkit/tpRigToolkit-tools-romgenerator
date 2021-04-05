#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-romgenerator model implementation
"""

from __future__ import print_function, division, absolute_import

from Qt.QtCore import Signal, QObject

from tpDcc.libs.python import python


class RomGeneratorModel(QObject):

    rotateXChanged = Signal(bool)
    rotateYChanged = Signal(bool)
    rotateZChanged = Signal(bool)
    solveAsOneItemChanged = Signal(bool)
    intervalBetweenFramesChanged = Signal(int)
    animationStartFrameChanged = Signal(int)
    animationLengthChanged = Signal(int)
    sceneJointsChanged = Signal(dict)
    selectedJointsChanged = Signal(list)

    def __init__(self):
        super(RomGeneratorModel, self).__init__()

        self._rotate_x = True
        self._rotate_y = True
        self._rotate_z = True
        self._solve_as_one_item = False
        self._interval_between_frames = 10
        self._animation_start_frame = 0
        self._anim_length = '0'
        self._scene_joints = dict()
        self._selected_joints = list()

    @property
    def rotate_x(self):
        return self._rotate_x

    @rotate_x.setter
    def rotate_x(self, flag):
        self._rotate_x = bool(flag)
        self.rotateXChanged.emit(self._rotate_x)

    @property
    def rotate_y(self):
        return self._rotate_y

    @rotate_y.setter
    def rotate_y(self, flag):
        self._rotate_y = bool(flag)
        self.rotateYChanged.emit(self._rotate_y)

    @property
    def rotate_z(self):
        return self._rotate_z

    @rotate_z.setter
    def rotate_z(self, flag):
        self._rotate_z = bool(flag)
        self.rotateZChanged.emit(self._rotate_z)

    @property
    def solve_as_one_item(self):
        return self._solve_as_one_item

    @solve_as_one_item.setter
    def solve_as_one_item(self, flag):
        self._solve_as_one_item = bool(flag)
        self.solveAsOneItemChanged.emit(self._solve_as_one_item)

    @property
    def interval_between_frames(self):
        return self._interval_between_frames

    @interval_between_frames.setter
    def interval_between_frames(self, value):
        self._interval_between_frames = int(value)

    @property
    def animation_start_frame(self):
        return self._animation_start_frame

    @animation_start_frame.setter
    def animation_start_frame(self, value):
        self._animation_start_frame = int(value)
        self.animationStartFrameChanged.emit(self._animation_start_frame)

    @property
    def animation_length(self):
        return self._anim_length

    @animation_length.setter
    def animation_length(self, value):
        self._anim_length = int(value)
        self.animationLengthChanged.emit(self._anim_length)

    @property
    def scene_joints(self):
        return self._scene_joints

    @scene_joints.setter
    def scene_joints(self, joints_dict):
        self._scene_joints = joints_dict
        self.sceneJointsChanged.emit(self._scene_joints)

    @property
    def selected_joints(self):
        return self._selected_joints

    @selected_joints.setter
    def selected_joints(self, joints_list):
        self._selected_joints = python.force_list(joints_list)
        self.selectedJointsChanged.emit(self._selected_joints)
