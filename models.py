import datetime

from app import db

class User(db.Model):
	__tablename__ = 'user'

	# start your code after this line
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), unique = True, nullable = False)
	contact_number = db.Column(db.Integer, unique = True, nullable = False)

	#one-to-many model
	temperature = db.relationship('Temperature', back_populates = 'user', uselist = True)
	# end your code before this line

	def __init__(self, name, contact_number):
		# start your code after this line
		self.name = name
		self.contact_number = contact_number
		# end your code before this line

	def serialize(self):
		# start your code after this line
		return {
			'name' : self.name,
			'contact_number' : self.contact_number
				}
		# end your code before this line

class Temperature(db.Model):
	__tablename__ = 'temperature'

	# start your code after this line
	id = db.Column(db.Integer, primary_key = True)
	timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow)
	temp_value = db.Column(db.Float, unique = False, nullable = False)
	user_name = db.Column(db.String(50), db.ForeignKey('user.name'))

	user = db.relationship('User', back_populates = 'temperature')

	# end your code before this line

	def __init__(self, temp_value, user_name):
		# start your code after this line
		self.temp_value = temp_value
		self.user_name = user_name
		# end your code before this line

	def serialize(self):
		# start your code after this line
		return {
			'id' : self.id,
			'temp_value' : self.temp_value,
			'timestamp' : self.timestamp,
			'user_id' : self.user.id,
			'user_name' : self.user_name
		}
		# end your code before this line

