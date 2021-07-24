from flask import Flask, request, render_template, jsonify
import os
import random
import json
from balloons import World
from balloons import Weather_balloon

 
basedir = os.path.abspath(os.path.dirname(__file__))    

app = Flask(__name__)

# Set up a secret key that is used to encrypt and decrypt some items passed
# to the browser 
app.config["SECRET_KEY"] = "We just need a secret here: I like yellow."

@app.route("/")
def index(): 
    rendered_html = render_template("index.html")
    return rendered_html
   
@app.route("/balloon_world") 
def balloon_world():
    number_of_balloons = int(random.random() * 10) 

    balloons = [] 

    # create world 
    created_world = World()   

    #create balloons   

    for _balloon in range(number_of_balloons):
        balloon = {}
        created_balloon = Weather_balloon()
        print(created_balloon.location) 
        balloon["location"] = created_balloon.location
        print(created_balloon.balloon_colour)
        balloon["colour"] = created_balloon.balloon_colour
        print(created_balloon.balloon_name)
        balloon["name"] = created_balloon.balloon_name 

        print(balloon)  
        balloons.append(balloon)       

    created_world_name = created_world.name 
    created_world_colour = created_world.colour          

    
   
    balloons_as_json = json.dumps(balloons)           
      
    

    return jsonify(dict(number_of_balloons = number_of_balloons, created_world_name = created_world_name, created_world_colour = created_world_colour, balloons_as_json = balloons_as_json))
                        
                        
      


"""not sure if need this route""" 
@app.route("/display_balloon_world")
def display_balloon_world(): 
    rendered_html = render_template("display_balloon_world.html")   
    return rendered_html                 
   
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0") 