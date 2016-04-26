# -*- coding: utf-8 -*-

"""
	Project Bluebox

	Copyright (C) <2015> <University of Stuttgart>

	This software may be modified and distributed under the terms
	of the MIT license.  See the LICENSE file for details.
"""

import logging
from flask import Flask


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(module)s -  %(funcName)s - %(levelname)s ##\t  %(message)s")
log = logging.getLogger()

app = Flask(__name__)

import mcm.retentionManager.apiServer