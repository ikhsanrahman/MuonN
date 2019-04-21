import datetime

from flask import request, make_response, jsonify
from flask_restplus import Resource

from app.api.user.serializer import *
from app.api.user.model import UserProcess
from app.api.user.request_schema import *
from app.api.config import config 
from app.api.namespace import User

api = User.api


@api.route('')
class Event(Resource):

    @api.doc('list user')
    def get(self):
        result = UserProcess().list()
        return result

    @api.doc('register user')
    def post(self):
        
        payload = UserRequestSchema().parser.parse_args(strict=True)
        errors = UserSerializer().load(payload).errors
        if errors :
            return errors

        result = UserProcess().create(payload)
        return result
    #end def







