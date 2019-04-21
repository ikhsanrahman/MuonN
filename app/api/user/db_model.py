from app.api.create_app import db
from app.api.config.config import Config 

TIME = Config.time()

class User(db.Model):
	__tablename__ = 'users'

	id	 					= db.Column(db.Integer, primary_key=True, autoincrement=True)
	name		 			= db.Column(db.String(255))
	email					= db.Column(db.String(255))
	# password 				= db.Column(db.String(255))
	phone					= db.Column(db.String(255))
	program 				= db.Column(db.String(255))
	pekerjaan 				= db.Column(db.String(255))
	alamat					= db.Column(db.String(255))
	registered_at			= db.Column(db.DateTime, default=TIME)
	deleted_at				= db.Column(db.DateTime)
	removed_at				= db.Column(db.DateTime)
	# programs 				= db.ForeingKey('Program')


	def __repr__(self):
		return "<{} has registered successfully".format(self.name)






# class Program(db.Model):
# 	__tablename__ = "program"

# 	id 					= db.Column(db.Integer, primary_key=True)
# 	name				= db.Column(db.Text)
# 	created_at

