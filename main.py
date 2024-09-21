import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import serverless_wsgi

from analyze import image_analyzer

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["GET"])
def chat_test():
    return 'App is working...'

@app.route("/analyze", methods=["POST"])
def chat():
    imageUrl = request.form.get('imageUrl', '')

    result = {}

    if imageUrl:
        result = image_analyzer(imageUrl)
    # if imagefile:
    #     return image_analyzer(imagefile)
    
    return jsonify(result)



def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)

if __name__ == "__main__":
    app.run(debug=True)