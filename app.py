from flask import Flask, request, render_template
from random import choice, sample 
import  random
import requests
import json
import os #creating a enviromental variable : so our api key and id won't get pushed to github or remotely.
# from YelpAPI import get_my_key
import pprint #pyhton json viewer  libary

app = Flask(__name__)

stars = {"oneStar": "⭐️",
         "twoStar": "⭐️ ⭐️",
         "threeStar": "⭐️ ⭐️ ⭐️",
         "fourStar": "⭐️ ⭐️ ⭐️ ⭐️",
         "fiveStar": "⭐️ ⭐️ ⭐️ ⭐️ ⭐️"}

# Yelp business info API request url
business_id = 'adLzMuVhL1CSj0j0VeXTZQ'


API_KEY = 'P8HZvWFwVupqzc7RTaLgjHxRIN0f6E380U6ZpIFCJaPZl-ButUiJlrTq89KVnDkRuesCGBinXj8MPqiUL_KT9ooFU1xHsDe72NBVDWO_MhmKDKpOgUHOASvVG6GiXXYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
# key = 'P8HZvWFwVupqzc7RTaLgjHxRIN0f6E380U6ZpIFCJaPZl-ButUiJlrTq89KVnDkRuesCGBinXj8MPqiUL_KT9ooFU1xHsDe72NBVDWO_MhmKDKpOgUHOASvVG6GiXXYx'
HEADERS = {"Authorization": "bearer %s" % API_KEY}

#home route 
@app.route('/')
def home():
   

  
   return render_template("index.html")

# show result base on what user enter in seach box
@app.route("/showResult")
def showResult():

    search = request.args.get("term")
    location = request.args.get("city")
    # this is usually right behind the url of API address
    PARAMETERS = {  "term": search,
                    "location": location
                # "key": key
                }

    r = requests.get(url = ENDPOINT,
                    params=PARAMETERS,
                    headers=HEADERS)

    business_json = r.json()
    # pp = pprint.PrettyPrinter(indent=4) #indexting by four 
    # pp.pprint(business_json) #print data from yelp
    # #three_messages = sample(messages, 3)

    return render_template("show_Business.html", stars=stars,  business_json=business_json)





if __name__ == "__main__":
    app.run(debug=True)