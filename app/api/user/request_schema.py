# from werkzeug.datastructures import FileStorage


from flask_restplus import reqparse

class UserRequestSchema:
	"""Define all mandatory argument for creating User"""
	parser = reqparse.RequestParser()
	parser.add_argument("name",    		 	type=str, required=True)
	parser.add_argument("email",        	type=str, required=True)
	parser.add_argument("phone",   		 	type=str, required=True)
	parser.add_argument("program", 		 	type=str, required=True)
	parser.add_argument("pekerjaan",		type=str, required=True)
	parser.add_argument("alamat", 		 	type=str, required=True)
#end class

