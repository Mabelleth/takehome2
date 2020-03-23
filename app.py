# Step 01: import necessary libraries/modules
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# your code begins here 

# Step 02: initialize flask app here 
app = Flask(__name__)
app.debug = True

# Step 03: add database configurations here
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://asm02user:password@localhost:5432/asm02db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Step 04: import models
from models import User, Temperature

# Step 05: add routes and their binded functions here
@app.route('/user/', methods=['POST']) 
def create_user():
	print('create_user')

	# start your code after this line

	# end your code before this line

@app.route('/temp/', methods=['POST']) 
def create_temp():
	print('create_temp')

	# start your code after this line

	# end your code before this line

@app.route('/friend/', methods=['PUT']) 
def update_friend():
	print('update_friend')

	# start your code after this line

	# end your code before this line

@app.route('/user/', methods=['GET']) 
def get_user():
	print('get_user')

	# start your code after this line

	# end your code before this line

@app.route('/temp/', methods=['GET']) 
def get_temp():
	print('get_temp')

	# start your code after this line

	# end your code before this line

# your code ends here 

if __name__ == '__main__':
	app.run(debug=True)
