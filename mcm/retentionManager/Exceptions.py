#!/usr/bin/python
# coding=utf-8

"""
	Project MCM - Micro Content Management
	RetentionManager - Swift API proxy and retention date checker


	Copyright (C) <2016> Tim Waizenegger, <University of Stuttgart>

	This software may be modified and distributed under the terms
	of the MIT license.  See the LICENSE file for details.
"""
from flask import jsonify


def raiseHttpError(msg, status_code):
	raise HttpError(msg, status_code)


class HttpError(Exception):
	status_code = 400

	def __init__(self, message, status_code=None):
		Exception.__init__(self)
		self.message = message
		if status_code is not None:
			self.status_code = status_code

	def to_json(self):
		d = {"message": self.message}
		json = jsonify(d)
		return json

	def to_string(self):
		return self.message
