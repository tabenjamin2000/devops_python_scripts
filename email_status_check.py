### A python code that takes user email address as input and checks it then tells the user if the email is valid or not.
### Prerequisite - pip3 install email_validator

from email_validator import validate_email, EmailNotValidError

def verify_status(email):
	try:
		_status = validate_email(email)
		print("Success!! You have entered a valid email")
	except EmailNotValidError as error_message:
		print(str(error_message))

_email = input("Please enter your email: ")
verify_status(_email)
