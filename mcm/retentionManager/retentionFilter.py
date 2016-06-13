#!/usr/bin/python
# coding=utf-8

"""
	Project MCM - Micro Content Management
	RetentionManager - Swift API proxy and retention date checker


	Copyright (C) <2016> Tim Waizenegger, <University of Stuttgart>

	This software may be modified and distributed under the terms
	of the MIT license.  See the LICENSE file for details.
"""

from functools import wraps
import logging
import dateutil.parser
import datetime
from flask import request, Response, send_file
import json

from mcm.retentionManager import app, httpBackend, appConfig
from mcm.retentionManager.Exceptions import HttpError, raiseHttpError
import swiftclient

"""WSGI application for the proxy server."""

RETENTIONFIELD = 'x-object-meta-mgmt-retentiondate'

log = logging.getLogger()


##############################################################################
# decorators
##############################################################################
def checkRetentionDate(f):
	@wraps(f)
	def checkRetentionDate_wrapper(*args, **kwargs):
		log.debug("checking retention date: {} {}".format(request.method, request.url))
		if ('DELETE' == request.method):
			# log.warning("is a delete! {}".format(kwargs))
			retentionDate = getRetentionDate(
				authName=kwargs["thisAuth"],
				authToken=request.headers["X-Auth-Token"],
				containerName=kwargs["thisContainer"],
				objectName=kwargs["thisObject"]
			)
			if retentionDate:
				log.warning("request is a delete! retention is {}".format(retentionDate))
				if not isRetentionOver(retentionDate):
					log.error("Deletion denied: Object is in retention {}".format(kwargs["thisObject"]))
					return raiseHttpError("Object is in retention until {}".format(retentionDate), 423)
		return f(*args, **kwargs)

	return checkRetentionDate_wrapper


##############################################################################
# swift api
##############################################################################
def getRetentionDate(authName, authToken, containerName, objectName):
	c = getSwiftClient(authName, authToken)
	h = c.head_object(containerName, objectName)
	t = h.get(RETENTIONFIELD, None)
	if t:
		try:
			d = dateutil.parser.parse(t)
			return d
		except Exception:
			log.exception(
				"could not parse retention date -- {} -- on obj: {} in {}".format(t, objectName, containerName))
	return None


def isRetentionOver(retentionDate):
	now = datetime.datetime.now(dateutil.tz.tzutc())
	return retentionDate < now


def getSwiftClient(authName, authToken):
	su = appConfig.swift_storage_url.format(authName)
	return swiftclient.client.Connection(
		preauthtoken=authToken,
		preauthurl=su
	)
