from flask import Flask, request, render_template
from random import choice
from random import sample 
import requests
import json
import os #creating a enviromental variable : so our api key and id won't get pushed to github or remotely.


app = Flask(__name__)

messages = ["Wow you is beautiful", "Awesome", "Lets get marry", "Precious", "Your are so awesome"]

# Yelp business info API request url
# https://api.yelp.com/v3/businesses/{id}

id = 'adLzMuVhL1CSj0j0VeXTZQ'
key = 'P8HZvWFwVupqzc7RTaLgjHxRIN0f6E380U6ZpIFCJaPZl-ButUiJlrTq89KVnDkRuesCGBinXj8MPqiUL_KT9ooFU1xHsDe72NBVDWO_MhmKDKpOgUHOASvVG6GiXXYx'


#home route 
@app.route('/')
def home():
   

  
   return render_template("index.html")

# show result base on what user enter in seach box
@app.route("/showResult")
def showResult():

    search = request.args.get("storeName")
    # this is usually right behind the url of API address
    params = {  "term": search,
                "key": key
                }

    r = requests.get("https://api.yelp.com/v3/businesses/search",id=params)
    jokes_json = r.json()
    # print(jokes_json)
    #three_messages = sample(messages, 3)

    return f"user entered: {search} {jokes_json}"





if __name__ == "__main__":
    app.run(debug=True)