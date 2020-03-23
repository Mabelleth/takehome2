import datetime

from app import db

class User(db.Model):
	__tablename__ = 'user'

	# start your code after this line

	# end your code before this line

	def __init__(self, name, contact_number):
		# start your code after this line

		# end your code before this line

	def serialize(self):
		# start your code after this line

		# end your code before this line

class Temperature(db.Model):
	__tablename__ = 'temperature'

	# start your code after this line

	# end your code before this line

	def __init__(self, temp_value, user_id):
		# start your code after this line

		# end your code before this line

	def serialize(self):
		# start your code after this line

		# end your code before this line