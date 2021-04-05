#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-romgenerator server implementation for Maya
"""

from tpDcc.core import server


class RomGeneratorServer(server.DccServer, object):

    PORT = 45322
