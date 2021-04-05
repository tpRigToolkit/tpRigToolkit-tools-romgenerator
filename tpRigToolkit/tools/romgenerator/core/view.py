#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains view implementation for tpRigToolkit-tools-romgenerator
"""

from __future__ import print_function, division, absolute_import

from Qt.QtCore import Qt
from Qt.QtWidgets import QSizePolicy, QWidget, QListWidget, QListWidgetItem, QSplitter

from tpDcc.managers import resources
from tpDcc.libs.qt.core import base, contexts as qt_contexts
from tpDcc.libs.qt.widgets import layouts, label, buttons, checkbox, spinbox, dividers, search


class RomGeneratorView(base.BaseWidget):
    def __init__(self, model, controller, parent=None):

        self._model = model
        self._controller = controller

        super(RomGeneratorView, self).__init__(parent=parent)

        self.refresh()

    # =================================================================================================================
    # OVERRIDES
    # =================================================================================================================

    def ui(self):
        super(RomGeneratorView, self).ui()

        main_splitter = QSplitter(parent=self)
        main_splitter.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        joints_list_widget = QWidget(parent=self)
        joints_list_layout = layouts.VerticalLayout(spacing=2, margins=(2, 2, 2, 2))
        joints_list_widget.setLayout(joints_list_layout)
        self._search = search.SearchFindWidget(parent=self)
        self._joints_list = QListWidget(parent=self)
        self._joints_list.setSelectionMode(QListWidget.ExtendedSelection)
        joints_list_layout.addWidget(self._search)
        joints_list_layout.addWidget(dividers.Divider(parent=self))
        joints_list_layout.addWidget(self._joints_list)

        options_widget = QWidget(parent=self)
        options_main_layout = layouts.VerticalLayout(spacing=0, margins=(0, 0, 0, 0))
        options_widget.setLayout(options_main_layout)
        options_layout = layouts.GridLayout()
        self._rotate_x_cbx = checkbox.BaseCheckBox('Rotate X', parent=self)
        self._rotate_y_cbx = checkbox.BaseCheckBox('Rotate Y', parent=self)
        self._rotate_z_cbx = checkbox.BaseCheckBox('Rotate Z', parent=self)
        self._solve_one_item_cbx = checkbox.BaseCheckBox('Solve as One Item', parent=self)
        self._interval_frames_spn = spinbox.BaseSpinBox(parent=self)
        self._anim_start_frame_spn = spinbox.BaseSpinBox(parent=self)
        self._current_anim_length_lbl = label.BaseLabel(parent=self)
        self._generate_rom_button = buttons.BaseButton('Generate Range of Motion Keys', parent=self)
        self._clear_rom_button = buttons.BaseButton(parent=self)
        self._clear_rom_button.theme_type = buttons.BaseButton.Types.DANGER
        self._clear_rom_button.setIcon(resources.icon('trash'))
        self._clear_rom_button.setStyleSheet('background-color: rgba(')
        self._clear_rom_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        buttons_layout = layouts.HorizontalLayout(spacing=2, margins=(2, 2, 2, 2))
        buttons_layout.addWidget(self._generate_rom_button)
        buttons_layout.addWidget(self._clear_rom_button)
        options_layout.addWidget(self._rotate_x_cbx, 0, 0)
        options_layout.addWidget(self._rotate_y_cbx, 0, 1)
        options_layout.addWidget(self._rotate_z_cbx, 0, 2)
        options_layout.addWidget(self._solve_one_item_cbx, 1, 0)
        options_layout.addWidget(label.BaseLabel('Interval Between Frames:', parent=self), 2, 0, Qt.AlignRight)
        options_layout.addWidget(self._interval_frames_spn, 2, 1, 1, 2)
        options_layout.addWidget(label.BaseLabel('Animation Start Frame:', parent=self), 3, 0, Qt.AlignRight)
        options_layout.addWidget(self._anim_start_frame_spn, 3, 1, 1, 2)
        options_layout.addWidget(label.BaseLabel('Current Animation Length:', parent=self), 4, 0, Qt.AlignRight)
        options_layout.addWidget(self._current_anim_length_lbl, 4, 1, 1, 2)
        options_main_layout.addLayout(options_layout)
        options_main_layout.addStretch()
        options_main_layout.addWidget(dividers.Divider(parent=self))
        options_main_layout.addLayout(buttons_layout)

        self.main_layout.addWidget(main_splitter)
        main_splitter.addWidget(joints_list_widget)
        main_splitter.addWidget(options_widget)

    def setup_signals(self):
        self._rotate_x_cbx.toggled.connect(self._controller.set_rotate_x)
        self._rotate_y_cbx.toggled.connect(self._controller.set_rotate_y)
        self._rotate_z_cbx.toggled.connect(self._controller.set_rotate_z)
        self._solve_one_item_cbx.toggled.connect(self._controller.set_solve_as_one_item)
        self._interval_frames_spn.valueChanged.connect(self._controller.set_interval_frames)
        self._anim_start_frame_spn.valueChanged.connect(self._controller.set_animation_start_frame)
        self._joints_list.itemSelectionChanged.connect(self._on_joints_selection_changed)
        self._generate_rom_button.clicked.connect(self._controller.generate_rom)
        self._clear_rom_button.clicked.connect(self._controller.clear_rom)

        self._model.rotateXChanged.connect(self._on_rotate_x_changed)
        self._model.rotateYChanged.connect(self._on_rotate_y_changed)
        self._model.rotateZChanged.connect(self._on_rotate_z_changed)
        self._model.solveAsOneItemChanged.connect(self._on_solve_as_one_item_changed)
        self._model.intervalBetweenFramesChanged.connect(self._on_interval_between_frames_changed)
        self._model.animationStartFrameChanged.connect(self._on_animation_start_frame_changed)
        self._model.animationLengthChanged.connect(self._on_animation_length_changed)
        self._model.sceneJointsChanged.connect(self._on_scene_joints_changed)

    # =================================================================================================================
    # BASE
    # =================================================================================================================

    def refresh(self):
        self._rotate_x_cbx.setChecked(self._model.rotate_x)
        self._rotate_y_cbx.setChecked(self._model.rotate_y)
        self._rotate_z_cbx.setChecked(self._model.rotate_z)
        self._solve_one_item_cbx.setChecked(self._model.solve_as_one_item)
        self._interval_frames_spn.setValue(self._model.interval_between_frames)
        self._anim_start_frame_spn.setValue(self._model.animation_start_frame)
        self._current_anim_length_lbl.setText(str(self._model.animation_length))

        # This updates the model and that forces the update of the view
        self._controller.update_scene_joints()

    # =================================================================================================================
    # CALLBACKS
    # =================================================================================================================

    def _on_rotate_x_changed(self, flag):
        with qt_contexts.block_signals(self._rotate_x_cbx):
            self._rotate_x_cbx.setChecked(flag)

    def _on_rotate_y_changed(self, flag):
        with qt_contexts.block_signals(self._rotate_y_cbx):
            self._rotate_y_cbx.setChecked(flag)

    def _on_rotate_z_changed(self, flag):
        with qt_contexts.block_signals(self._rotate_z_cbx):
            self._rotate_z_cbx.setChecked(flag)

    def _on_solve_as_one_item_changed(self, flag):
        with qt_contexts.block_signals(self._solve_one_item_cbx):
            self._solve_one_item_cbx.setChecked(flag)

    def _on_interval_between_frames_changed(self, value):
        with qt_contexts.block_signals(self._interval_frames_spn):
            self._interval_frames_spn.setValue(value)

    def _on_animation_start_frame_changed(self, value):
        with qt_contexts.block_signals(self._anim_start_frame_spn):
            self._anim_start_frame_spn.setValue(value)

    def _on_animation_length_changed(self, value):
        with qt_contexts.block_signals(self._current_anim_length_lbl):
            self._current_anim_length_lbl.setText(str(value))

    def _on_scene_joints_changed(self, scene_joints_data):
        self._joints_list.clear()
        joint_names = scene_joints_data.get('names', list())
        joint_handles = scene_joints_data.get('handles', list())
        for joint_name, joint_handle in zip(joint_names, joint_handles):
            joint_item = QListWidgetItem(joint_name)
            joint_item.setIcon(resources.icon('bone'))
            joint_item.setData(Qt.UserRole + 1, joint_handle)
            self._joints_list.addItem(joint_item)

    def _on_joints_selection_changed(self):
        selected_items = self._joints_list.selectedItems()
        joints_uuids = [item.data(Qt.UserRole + 1) for item in selected_items]
        self._controller.set_selected_joints(joints_uuids)
