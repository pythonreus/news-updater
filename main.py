from flask import Flask
import news,mail,weather

app = Flask(__name__)

# response for all my functions will be in the form {error = string, data = {},status = int}

@app.route("/")
def home_route():
	return "hello world"



