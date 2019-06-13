#Importing flask
#Render_template helps us use templates for pages
#url_for helps us import css static files
from flask import Flask,render_template,url_for

#Creating a variable app
#Flask knows where do look for templates,etc
app = Flask(__name__)

#Creating a dummy post using a list of dictionaries

posts=[
    {
        'author':'Saurabh Kulkarni',
        'title':'Blog Post 1',
        'content':'First blog post content',
        'date_posted':'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second blog post content',
        'date_posted': 'April 21, 2018'
    }




]


#What we type into our browser is created using app decorators
#Allows  us to write functions that will return text on our webpage
#You can have two routes doing the same thing, leading to same page

@app.route("/")
@app.route("/home")

#Function to print something on our page
#Here we use render_template which will run the html in file home.html instead of having html here
#We supply posts=posts that was defined above. ALl the variables in posts are now accessible in home.html
#We can use that in home.html to write content

def home():
    return render_template('home.html',posts=posts)

#Create an about route
@app.route("/about")

#Function to print something on our page
#We pass in title argument that is specified in html template
def about():
    return render_template('about.html',title='About Saurabh')


#NOTE
#Before running this for the first time, set environment variable in terminal using "export FLASK_APP=flaskblog.py"
#For your Ubuntu system, run conda activate to go into conda environment and then run flask run


#To avoid setting app environment variables all the time when we want to run the program we do this
#We set debug true so that we do not need to restart server everytime we make changes

if __name__=='__main__':
    app.run(debug=True)