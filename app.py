from flask import Flask, request, render_template
from random import choice
from random import sample 


app = Flask(__name__)

messages = ["Wow you is beautiful", "Awesome", "Lets get marry", "Precious", "Your are so awesome"]

#home route 
@app.route('/')
def home():
   
  
   return render_template("index.html")

# show result base on what user enter in seach box
@app.route("/showResult")
def showResult():

    search = request.args.get("name")
    three_messages = sample(messages, 3)

    return f"user entered: {search}, {three_messages}"





if __name__ == "__main__":
    app.run(debug=True)