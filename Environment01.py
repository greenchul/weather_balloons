

class Environment:

    def __init__(self, canvas_y):
        self.name = "standard_atmosphere"
        self.surface_pressure = 1013.25
        self.lapse_rate = 2
        self.outside_air_temperature = 15
        self.canvas_y = canvas_y
        self.popping_height = 70000
        self.single_y_unit = self.calculate_y_unit()

    def calculate_y_unit(self):
        single_y_unit_ft = self.popping_height / self.canvas_y
        return single_y_unit_ft

    def calculate_height_in_feet(self, y_position):
        ground_level = self.canvas_y/2
        height_in_feet = ((y_position + ground_level) * self.single_y_unit) 
        return height_in_feet





if __name__ == "__main__":
    my_environment = Environment(600)
    print(my_environment.name)
    print(my_environment.single_y_unit)
    print(my_environment.calculate_height_in_feet(300))
    print(my_environment.calculate_height_in_feet(-300))
    print(my_environment.calculate_height_in_feet(0))
