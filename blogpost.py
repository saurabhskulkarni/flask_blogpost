#Importing flask
from flask import Flask
#Creating a variable app
#Flask knows where do look for templates,etc
app = Flask(__name__)


#What we type into our browser is created using app decorators
#Allows  us to write functions that will return text on our webpage
#You can have two routes doing the same thing, leading to same page
@app.route("/")
@app.route("/home")
#Function to print something on our page
def home():
    return "<h1>Hello Saurabh Kulkarni!</h1>"

#Create an about route

@app.route("/about")

#Function to print something on our page
def about():
    return "<h1>About Page</h1>"


#NOTE
#Before running this for the first time, set environment variable in terminal using "export FLASK_APP=flaskblog.py"
#For your Ubuntu system, run conda activate to go into conda environment and then run flask run


#To avoid setting app environment variables all the time when we want to run the program we do this
if __name__=='__main__':
    app.run(debug=True)