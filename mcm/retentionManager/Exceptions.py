'''
Created on Feb 11, 2016

@author: mcm
'''
from flask import jsonify

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