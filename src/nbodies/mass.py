import numpy as np



class massObject:
    def __init__(self, mass, position, velocity, objectRadius):
        self.mass = mass
        self.pos = position
        self.vel = velocity
        self.coreDist = objectRadius

        # Gravitational Constant
        global G
        G = 6.674 * 10**-11

    # Get mass object attribute functions
    def getMass(self):
        return self.mass
    
    def getPosition(self):
        return self.pos
    
    def getVelocity(self):
        return self.vel
    
    def getObjectRad(self):
        return self.coreDist
    
    # Set mass object attribute functions
    def setPosition(self, position):
        self.pos = position

    def setVelocity(self, velocity):
        self.vel = velocity

    
    # Functions to handle physics and movement
    
    # Acceleration due to gravity function
    def accelerate(self, otherObject):
        # Magnitute of distance
        MagPos = self.distance(otherObject)

        # Unit vector of position
        unitV = (self.pos - otherObject.getPosition()) / MagPos

        # Calculate acceleration due to gravity
        a = -(G * otherObject.getMass()) / (MagPos**2)

        #print(a * unitV)
        return a * unitV
    
    # Distance between two objects
    def distance(self, otherObject):
        diff = self.pos - otherObject.getPosition()
        return np.linalg.norm(diff)