


#----------------- modeling to process anything related to user -----------------#

from flask import jsonify

from app.api.create_app import db
from app.api.user.db_model import User
from app.api.config.config import Config
from app.api.user.serializer import * 




TIME = Config.time()

class UserProcess:


	def create(self, payload):
		# event = Event.query.filter_by(event=payload['event']).first()

		new_user = User(name=payload['name'], email=payload['email'], \
								phone=payload['phone'], program=payload['program'],\
								pekerjaan=payload['pekerjaan'], alamat=payload['alamat'])

		db.session.add(new_user)
		db.session.commit()

		return jsonify(message="user has been registered")

	def list(self):
		users = User.query.all()

		output = []

		if users:
			result = UserSerializer(many=True).dump(users).data
			return jsonify(result)

		if not users:
			return jsonify(message="user not available")



