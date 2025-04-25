# Base class representing a general vehicle
class Vehicle:
    def move(self):
        print("This vehicle moves in some way.")
        
# Subclass representing a car
class Car(Vehicle):
    def move(self):
        # Generic movement method
        print(" This vehicle moves in some way.")
        
# Subclass representing a car
class Car(Vehicle):
    def move(self):
        #override move to represent driving
        print("Driving")
        
# Subclass representing a plane
class Plane(Vehicle):
    def move(self):
        #override move to represent flying
        print("Flying")
        
# Subclass representing a boat
class Boat(Vehicle):
    def move(self):
        #override move to represent sailing
        print("Sailing")
        
# Subclass representing a bicycle
class Bicycle(Vehicle):
    def move(self):
        #override move to represent pedaling
        print("Pedaling")
        
# Create a list of different vehicle objects
Vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Demonstrate polymorphism by calling the same method.move()
# Each object responds in its own unique way
for v in Vehicles:
    v.move()                                        
        