import json
from flask import Flask,jsonify
import news,mail,weather
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# response for all my functions will be in the form {error = string, data = {},status = int}
@app.route("/",methods=['GET'])
def home_route():
	#display the weather and the current news
	return jsonify(news.get_all_news_updates())

@app.route("/single-article/<int:article_id>", methods=['GET'])
def single_route(article_id):
	return jsonify(news.get_single_news_update(article_id))


if __name__ == '__main__':
    app.run(debug=True)

