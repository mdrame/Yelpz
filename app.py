from flask import Flask, request, render_template
from random import choice
from random import sample 
import requests
import json


app = Flask(__name__)

messages = ["Wow you is beautiful", "Awesome", "Lets get marry", "Precious", "Your are so awesome"]

#home route 
@app.route('/')
def home():
   

  
   return render_template("index.html")

# show result base on what user enter in seach box
@app.route("/showResult")
def showResult():

    search = request.args.get("limitTo")
    # this is usually right behind the url of API address
    # params = {"store_Name": search}

    r = requests.get("http://api.icndb.com/jokes/random?limitTo=nerdy")
    jokes_json = r.json()
    # print(jokes_json)
    #three_messages = sample(messages, 3)

    return f"user entered: {search} {jokes_json}"





if __name__ == "__main__":
    app.run(debug=True)