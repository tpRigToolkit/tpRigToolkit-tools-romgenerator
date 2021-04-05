#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-romgenerator client implementation
"""

from tpDcc.core import client


class RomGeneratorClient(client.DccClient, object):

    PORT = 45322
