#!/usr/bin/python
# coding=utf-8

"""
	Project MCM - Micro Content Management
	RetentionManager - Swift API proxy and retention date checker


	Copyright (C) <2016> Tim Waizenegger, <University of Stuttgart>

	This software may be modified and distributed under the terms
	of the MIT license.  See the LICENSE file for details.
"""

import logging
from flask import Flask
from mcm.retentionManager import appConfig

logging.basicConfig(level=appConfig.log_level, format="%(asctime)s - %(module)s -  %(funcName)s - %(levelname)s ##\t  %(message)s")
log = logging.getLogger()

app = Flask(__name__)
import mcm.retentionManager.apiServer