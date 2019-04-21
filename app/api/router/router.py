

from flask_restplus import Api
from flask import Blueprint

from app.api.user.controller import api as user



blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='muon API ',
          version='1.0',
          
          )

api.add_namespace(user, path='/user')

