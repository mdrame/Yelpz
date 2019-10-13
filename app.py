from flask import Flask, request, render_template
from random import choice


app = Flask(__name__)

messages = ["Wow you is beautiful", "Awesome", "Lets get marry", "Precious", "Your are so awesome"]

#home route 
@app.route('/')
def home():
    #choosing one random picked index from the messages list and assign it to message variable/property.
    message = choice(messages)
    #getting data from an input in the base.html 
    name = request.args.get('name')
    return f"{message} : {name}"






if __name__ == "__main__":
    app.run(debug=True)