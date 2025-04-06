from flask import Flask
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)

# response for all my functions will be in the form {error = string, data = {},status = int}

@app.route("/")
def home_route():
	return "hello world"


def email_validator_address(email_address):
	try:
		is_valid = validate_email(email_address)
		return True, is_valid.email
	except EmailNotValidError as e:
		return False, str(e)

def schedule_sending_email():
	pass

def populate_news_database():
	pass	

def get_all_news_updates():
	pass

def get_single_news_update(news_id):
	pass

def delete_current_news_updates():
	pass

def get_weather_update(location):
	pass	

def send_email_updates(email_addr,weather,headlines):
	pass

def subscribe_to_newsletter(email_address):
	pass

def unsubscribe_to_newsletter(email_address):
	pass	


