#Importing flask
from flask import Flask
#Creating a variable app
#Flask knows where do look for templates,etc
app = Flask(__name__)


#What we type into our browser is created using app decorators
#Allows  us to write functions that will return text on our webpage
@app.route("/")

#Function to print something on our page
def hello():
    return "Hello World!"


#NOTE
#Before running this for the first time, set environment variable in terminal using "export FLASK_APP=flaskblog.py"
