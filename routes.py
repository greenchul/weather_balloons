from flask import Flask, request, render_template, jsonify
import os
import random
import json
from World import World 
world = World()
# from balloons import Weather_balloon

 
basedir = os.path.abspath(os.path.dirname(__file__))    

app = Flask(__name__)

# Set up a secret key that is used to encrypt and decrypt some items passed
# to the browser 
app.config["SECRET_KEY"] = "We just need a secret here: I like yellow."

@app.route("/") 
def index(): 
    rendered_html = render_template("index.html")
    return rendered_html
    
@app.route("/api_balloon_world") 
def api_balloon_world():
    # number_of_balloons = int(random.random() * 10)       

    return jsonify(world.get_world_data_for_api())  
                        
      
@app.route("/test")
def test():
    rendered_html = render_template("test.html")
    return rendered_html

"""not sure if need this route""" 
@app.route("/display_balloon_world") 
def display_balloon_world(): 
    rendered_html = render_template("display_balloon_world.html")         
    return rendered_html                 
   
    

 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0") 