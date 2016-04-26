# -*- coding: utf-8 -*-

"""
	Project Bluebox

	Copyright (C) <2015> <University of Stuttgart>

	This software may be modified and distributed under the terms
	of the MIT license.  See the LICENSE file for details.
"""

from mcm.retentionManager import app


import os

netPort = os.getenv("VCAP_APP_PORT", "4000")
netHost = os.getenv("VCAP_APP_HOST", "0.0.0.0")


"""
	Without threading, the server is too slow to serve clients. Requests are missed...
"""

app.run(
			host=netHost,
			port=int(netPort),
			debug=True,
			threaded=True
)