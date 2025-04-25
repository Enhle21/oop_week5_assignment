# CREATING A CLASS FOR SUPERHERO
# Base class representing a superhero
class Superhero:
    def __init__(self, name, power, city):
        # initializing superhero with a name, special power, and city they protect
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        # introduce the superhero
        print(f"Hello, I am {self.name} and I protect {self.city} with my {self.power}!")

    def use_power(self):
        # show how the superhero uses their power
        print(f"{self.name} uses {self.power} to save the day!")


# Subclass for a superhero with super speed
class Speedster(Superhero):
    def __init__(self, name, city, speed_level):
        # use the base class constructor with "super speed" as the power
        super().__init__(name, "super_speed", city)
        self._speed_level = speed_level  # encapsulation: private attribute

    def use_power(self):
        # override use_power to show specific speed action
        print(f"{self.name} zooms through {self.city} at speed level {self._speed_level}!")

    def get_speed_level(self):
        # getter method to access the private speed level
        return self._speed_level


# Subclass for a superhero who can fly
class Flyer(Superhero):
    def __init__(self, name, city, altitude_limit):
        # use the base class constructor with "flight" as the power
        super().__init__(name, "flight", city)
        self.altitude_limit = altitude_limit

    def use_power(self):
        # override use_power to show specific flying action
        print(f"{self.name} flies high up to {self.altitude_limit} meters above {self.city}!")


# Creating superhero objects with unique values
hero1 = Speedster("FlashStrike", "Johannesburg", "500ms")
hero2 = Flyer("Superman", "Cape Town", 5000)

# Call methods to see how they behave
hero1.introduce()
hero1.use_power()
hero2.introduce()
hero2.use_power()