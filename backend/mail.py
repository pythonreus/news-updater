from email_validator import validate_email, EmailNotValidError

def email_validator_address(email_address):
	try:
		is_valid = validate_email(email_address)
		return True, is_valid.email
	except EmailNotValidError as e:
		return False, str(e)


def send_verification_email(email_address,verification_link):
	pass 

def schedule_sending_email():
	pass

def send_email_updates(email_addr,weather,headlines):
	pass

def subscribe_to_newsletter(email_address):
	pass

def unsubscribe_to_newsletter(email_address):
	pass	
