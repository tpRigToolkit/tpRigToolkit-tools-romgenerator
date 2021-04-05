#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for tpRigToolkit-tools-romgenerator
"""

import pytest

from tpRigToolkit.tools.romgenerator import __version__


def test_version():
    assert __version__.get_version()
