# SUPERHERO and VEHICLE Polymorphism project


## Overview

This project demonstrates the concept of  Object-Oriented Programming (OOP) in Python,
focusing on Inheritence and Polymorphism.
1. "class.py": implements a superhero hierarchy with unique powers.
2. "poly.py": implement a vehicle hierarchy with different movement behaviors.


## Files
### 1. "class.py"
This file defines a hierarchy of superheroes with different ablities. It demonstrates:
- Inheritance: Subclasses inherit from a base "Superhero" class.
- Encapsulation: Private attributes are accessed using getter methods.
- Polymorphism: The "use_power()" method is overriden in subclasses tp provide unique behavior.


 ### Classes: 
 - Superhero: The base class representing a generic superhero.
     - Attributes: name, power, city
     - Methods: introduce(), use_power()
 - Speedster: A subclass representing a superhero with super speed.
     - Additional Attribute: _speed_level
     - Overriden Method: use_power()
 - Flyer: A subclass representing a superhero who can fly
     - Additional Attribute: altitude_limit
     - Overridden Method: use_power()
  

  ### Examples used:
  - hero1 = Speedster("flashstrike", "Johannesburg", "500ms")
  - hero2 = Flyer("Superman", "Cape Town, 5000)

  - hero1.introduce()
  - hero1.use_power()
  - hero2.introduce()
  - hero2.use_power()

  - OUTPUT: " Hello, I am Flashstrike and I protect Johannesburg with my super_speed!
    Flashstrike zooms through Johannesburg at speed level 500ms!
    Hello, I am Superman and I protect CapeTown with my flight!
    Superman flies high up to 5000 meters above Cape Town!


2.poly.py
This file defines a hierarchy of vehicles with different movement behaviour. It demonstrate:

- Polymorphism: The move() methos is overridden in subclasses to provide unique behaviour

Classes: 
- Vehicle: The base class representing a generic vehicle.
   - Method: move()
- Car: A subclass representing a car.
   - Overridden method: move() ( prints " Driving")
- Plane: A subclass representing a plane
   - Overridden method: move() (prints "Flying")
- Boat: A subclass  representing a boat.
   - Overridden method: move() (prints "Sailing")
- Bicycle: A subclass representing a bicycle.
  - Overridden method: move() (prints "Pedaling")


## Example used:
vehicle = [Car(), Plane(), Boat(), Bicycle()]
for v in vehicles: 
v.move()

## Output
- Driving
- Flying
- Sailing
- Pedaling


## Concept demonstrated
1. Inheritence
2. Polymorphism
3. Encapsulation
    
    
 
