import secrets
import random
import names
import threading
import time
import math

from Environment01 import Environment

## canvas height
canvas_height = 600
environment = Environment(canvas_height)

class World:
   
    def __init__(self):
        self.name = f"{names.get_last_name()}-{secrets.token_urlsafe(3)}"
        self.colour = (random.randrange(0,255), random.randrange(0,255),random.randrange(0,255))
        self.number_of_weather_balloons = random.randrange(2,5)
        self.weather_balloons = []
        self.maximum_z = 100
        self.maximum_x = 300
        self.maximum_y = canvas_height

        for _balloon_index in range(self.number_of_weather_balloons):
            balloon = Weather_balloon(maximum_z = self.maximum_z, maximum_x= self.maximum_x, maximum_y = self.maximum_y)
            self.weather_balloons.append(balloon)

    def get_world_data_for_api(self):
        world_data = {}
        world_data["name"] = self.name
        world_data["colour"] = self.colour
        world_data["number_of_weather_balloons"] = self.number_of_weather_balloons
        world_data["balloons"] = []
        
        for weather_balloon in self.weather_balloons:
            world_data["balloons"].append(weather_balloon.get_data())

        return world_data

    """
    Balloon class

    """
class Weather_balloon:
    def __init__(self, maximum_x = 300, maximum_z = 100, maximum_y = canvas_height):
        # self.maximum_altitude = maximum_altitude
        self.maximum_y = maximum_y
        self.maximum_x = maximum_x
        self.maximum_z = maximum_z
        self.location = [random.randrange(-self.maximum_x, self.maximum_x), -self.maximum_y/2, random.randrange(-self.maximum_z, self.maximum_z)]
        self.balloon_name = secrets.token_urlsafe(2)
        self.balloon_height_ft = environment.calculate_height_in_feet(self.location[1])
        self.balloon_temperature = environment.calculate_temperature(self.balloon_height_ft)
        self.balloon_pressure = environment.calculate_pressure(self.balloon_height_ft)
        self.balloon_red = 255
        self.balloon_green = 245
        self.balloon_blue = 230
        self.increase_altitude()


    def get_data(self):
        data = {}
        data["location"] = self.location
        data["balloon_name"] = self.balloon_name
        data["balloon_temperature"] = self.balloon_temperature
        data["balloon_red"]= self.balloon_red
        data["balloon_green"]= self.balloon_green
        data["balloon_blue"]= self.balloon_blue
        data["balloon_pressure"] = self.balloon_pressure
        data["balloon_height_ft"] = self.balloon_height_ft
        return data


    


    def increase_altitude(self):
        
        # now start moving anything that ready to be moved
        # Do the work in another thread to keep it fast
        kwargs = {}
        args = []
        threaded_function = self.increase_altitude_threaded
        thread = threading.Thread(
        target=threaded_function, args=args, kwargs=kwargs
        )
        thread.start()

    def increase_altitude_threaded(self):
        
        while True:
            self.location[1] = self.location[1] + random.randrange(1, 6)
            self.balloon_height_ft = math.floor(environment.calculate_height_in_feet(self.location[1]))
            self.balloon_temperature = environment.calculate_temperature(self.balloon_height_ft)
            self.balloon_pressure =  environment.calculate_pressure(self.balloon_height_ft)
            self.pop_balloon()

            time.sleep(1)

    def pop_balloon(self):
        if (self.balloon_height_ft > 20000):
            print(f"balloon {self.balloon_name} reached popping height")
            



    


if __name__ == "__main__":
    my_new_word = World()
    # print(my_new_word.name)

    # while True:
    #     print("about to sleep")
    #     time.sleep(0.5)
    



            
