import math

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

    def calculate_temperature(self, height01):
        height = height01/1000
        temperature = self.outside_air_temperature - (height * self.lapse_rate)
        return round(temperature, 1)

    def calculate_pressure(self, height01):
        ## first calculate temperature at given height - height is in feet
        height = height01/1000
        temp_in_degrees= self.outside_air_temperature - (height * self.lapse_rate)
        ## convert temp to kelvin ready for equation
        t = temp_in_degrees+273.15
        ## equation constants
        g = 9.80665
        M = 0.0289644
        gm = g*M
        # convert height to m ready for equation. 0 is reference level which is sea level so 0 
        height_cals = (height01/3.281) - 0
        ## R is universal gas constant
        R = 8.31432
        rt = R * t
        pressure = self.surface_pressure * math.exp((-gm*height_cals)/rt)
        ###   -gM(h-h₀)/(RT)
        return round(pressure, 1)





if __name__ == "__main__":
    my_environment = Environment(600)
    print(my_environment.name)
    # print(my_environment.single_y_unit)
    # print(my_environment.calculate_height_in_feet(300))
    # print(my_environment.calculate_height_in_feet(-300))
    # print(my_environment.calculate_height_in_feet(0))
    ## temperature tests
    print(my_environment.calculate_temperature(2456))
    print(my_environment.calculate_temperature(0))
    print(my_environment.calculate_pressure(0))
    print(my_environment.calculate_pressure(2000))
    print(my_environment.calculate_pressure(5000))
    print(my_environment.calculate_pressure(10000))
    # print(my_environment.calculate_pressure(609))