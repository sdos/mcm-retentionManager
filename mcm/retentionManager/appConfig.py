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

# log_level = logging.CRITICAL
# log_level = logging.ERROR
log_level = logging.WARNING
# log_level = logging.INFO
# log_level = logging.DEBUG
swift_auth_url = "http://192.168.209.204:8080/auth/v1.0"
swift_storage_url = "http://192.168.209.204:8080/v1/AUTH_{}"
proxy_storage_url = "http://localhost:4000/v1/AUTH_{}"
