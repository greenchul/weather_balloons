import secrets
import random
import names



class World:
   
    def __init__(self):
        self.name = f"{names.get_last_name()}-{secrets.token_urlsafe(3)}"
        self.colour = (random.randrange(0,255), random.randrange(0,255),random.randrange(0,255))
        
        

    """
    Balloon class

    """
class Weather_balloon:
    def __init__(self):
        self.location = (random.randrange(0,100), random.randrange(0,100))
        self.balloon_colour = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        self.balloon_name = secrets.token_urlsafe(2)

    def increase_height(self):
        self.height = 0

if __name__ == "__main__":
    my_new_word = World()
    print(my_new_word.name)
        



            
