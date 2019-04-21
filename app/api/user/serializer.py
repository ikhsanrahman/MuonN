import re

from marshmallow import Schema, fields, ValidationError, post_load, validates
from app.api.create_app import db


def cannot_be_blank(string):
	if not string:
		raise ValidationError(" Data cannot be blank")
#end def


class UserSerializer(Schema):
	id               	  			= fields.Integer()
	name	     	 	  			= fields.String(required=True, validate=cannot_be_blank)
	email   	    	      		= fields.String(required=True, validate=cannot_be_blank)
	phone           	  			= fields.String(required=True, validate=cannot_be_blank)
	program 		  				= fields.String(required=True, validate=cannot_be_blank)
	pekerjaan						= fields.String(required=True, validate=cannot_be_blank)
	alamat      	         		= fields.String(required=True, validate=cannot_be_blank)
	registered_at          			= fields.DateTime(attribute="regsitered_at")
	
		

	# def convert_bool_to_str(self, obj):
	# 	status = "ACTIVE"
	# 	if obj.status != True:
	# 		status = "INACTIVE"
	# 	return status
	# #end def

	@validates('name')
	def validate_name(self, name):
		
		pattern = r"^[a-z-A-Z ]+$"
		if len(name) < 2:
			raise ValidationError('Invalid {}. min is 2 character'.format(self.name))
		if len(name) > 100:
			raise ValidationError('Invalid {}, max is 40 character'.format(self.name))
		if  re.match(pattern, name) is None:
			raise ValidationError('Invalid {}. only alphabet is allowed'.format(self.name))
	#end def

	@validates('email')
	def validate_phone(self, email):
	
		pattern = r"^[a-z-A-Z0-9_@ ]+$"
		if len(email) < 5:
			raise ValidationError('Invalid email, min is 5 characters')
		if re.match(pattern, email) is None:
			raise ValidationError('Invalid email')

	@validates('phone')
	def validate_phone(self, phone):
		
		pattern = r"^[-0-9_ ]+$"
		if len(phone) < 6:
			raise ValidationError('Invalid {}. min is 6 character'.format(self.phone))
		if len(phone) > 15:
			raise ValidationError('Invalid {}, max is 15 character'.format(self.phone))
		if  re.match(pattern, phone) is None:
			raise ValidationError('Invalid {}. only alphanumeric is allowed'.format(self.phone))
	#end def

	@validates('program')
	def validate_program(self, program):
	
		pattern = r"^[a-z-A-Z0-9_ ]+$"
		if len(program) < 2:
			raise ValidationError('Invalid, min is 2 characters')
		if re.match(pattern, program) is None:
			raise ValidationError('Invalid program')

	@validates('pekerjaan')
	def validate_pekerjaan(self, pekerjaan):
		
		pattern = r"."
		if len(pekerjaan) < 2:
			raise ValidationError('Invalid {}. min is 2 character'.format(self.pekerjaan))
		if len(pekerjaan) > 100:
			raise ValidationError('Invalid {}, max is 100 character'.format(self.pekerjaan))
		if  re.match(pattern, pekerjaan) is None:
			raise ValidationError('Invalid {}. only alphanumeric is allowed'.format(self.pekerjaan))
	#end def

	@validates('alamat')
	def validate_alamat(self, alamat):
		
		pattern = r"."
		if len(alamat) < 2:
			raise ValidationError('Invalid {}. min is 2 character'.format(self.alamat))
		if len(alamat) > 100:
			raise ValidationError('Invalid {}, max is 100 character'.format(self.alamat))
		if  re.match(pattern, alamat) is None:
			raise ValidationError('Invalid {}'.format(self.alamat))
	#end def


