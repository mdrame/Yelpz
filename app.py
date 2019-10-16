from flask import Flask, request, render_template
from random import choice, sample 
import  random
import requests
import json
import os #creating a enviromental variable : so our api key and id won't get pushed to github or remotely.
# from YelpAPI import get_my_key
import pprint #pyhton json viewer  libary

app = Flask(__name__)

# # calliing long and lat from ip-api base on user IPAddress.
# def get_country(ip_address):

#         response = requests.get("http://ip-api.com/json/{}".format(ip_address))
#         js = response.json()
#         # city = js['countryCode']
#         return js
    # except Exception as e:
    #     return "Error : We cant seems to find your location, pls turn on your connectivity"

# stars = {"oneStar": "⭐️",
#          "twoStar": "⭐️ ⭐️",
#          "threeStar": "⭐️ ⭐️ ⭐️",
#          "fourStar": "⭐️ ⭐️ ⭐️ ⭐️",
#          "fiveStar": "⭐️ ⭐️ ⭐️ ⭐️ ⭐️"}

# Yelp business info API request url
business_id = 'adLzMuVhL1CSj0j0VeXTZQ'

#yelp Api Keys and ID
API_KEY = 'P8HZvWFwVupqzc7RTaLgjHxRIN0f6E380U6ZpIFCJaPZl-ButUiJlrTq89KVnDkRuesCGBinXj8MPqiUL_KT9ooFU1xHsDe72NBVDWO_MhmKDKpOgUHOASvVG6GiXXYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
# key = 'P8HZvWFwVupqzc7RTaLgjHxRIN0f6E380U6ZpIFCJaPZl-ButUiJlrTq89KVnDkRuesCGBinXj8MPqiUL_KT9ooFU1xHsDe72NBVDWO_MhmKDKpOgUHOASvVG6GiXXYx'
HEADERS = {"Authorization": "bearer %s" % API_KEY}


# IP-API url
ip_Url = "http://ip-api.com/json/"

#home route 
@app.route('/')
def home():
   
    # got Api from remote_addr
    ip_address = request.remote_addr
    # this is usually right behind the url of API address
    PARAMETERS = {"city": ip_address}
    #calling API
    respond = requests.get(ip_Url, params=PARAMETERS,)

    dic_of_datas = respond.json()
    city = dic_of_datas['city']
    print(city)
    
    # number of countries where the largest number of speakers are French
    # data from http://download.geonames.org/export/dump/countryInfo.txt
    # if country in ('BL', 'MF', 'TF', 'BF', 'BI', 'BJ', 'CD', 'CF', 'CG', 'CI', 'DJ', 'FR', 'GA', 'GF', 'GN', 'GP', 'MC', 'MG', 'ML', 'MQ', 'NC'):
    #     return "Bonjour"
        #testing
    # return "Hello"

  
    return render_template("index.html", city=city)

# show result base on what user enter in seach box
@app.route("/showResult")
def showResult():

#calling yelp fusion api
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

    #error handing to let user know that there is no match
    # if not business_json:
    #     no_business_found = " Sorry No bussiness match you search "
    #     return

    return render_template("show_Business.html", stars=stars,  business_json=business_json)





if __name__ == "__main__":
    app.run(debug=True)