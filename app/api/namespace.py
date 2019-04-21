from flask_restplus import Namespace, fields

class Home:
	api = Namespace('Home', description='api related to first access')

class User :
	''' class for Data Transfer Operation '''
	api = Namespace('User', description='api related to User')
