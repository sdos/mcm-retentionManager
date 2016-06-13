#!/usr/bin/python
# coding=utf-8

"""
	Project MCM - Micro Content Management
	RetentionManager - Swift API proxy and retention date checker


	Copyright (C) <2016> Tim Waizenegger, <University of Stuttgart>

	This software may be modified and distributed under the terms
	of the MIT license.  See the LICENSE file for details.
"""

from mcm.retentionManager import app


import os

netPort = os.getenv("VCAP_APP_PORT", "4000")
netHost = os.getenv("VCAP_APP_HOST", "127.0.0.1")


"""
	Without threading, the server is too slow to serve clients. Requests are missed...
"""

app.run(
			host=netHost,
			port=int(netPort),
			debug=True,
			threaded=True
)