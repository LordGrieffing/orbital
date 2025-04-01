import numpy as np



class massObject:
    # Gravitational Constant
    G = 6.674 * 10**-11

    # Constructor 
    def __init__(self, mass, position, velocity, objectRadius):
        self._mass = mass
        self._pos = position
        self._vel = velocity
        self._coreDist = objectRadius

    # Property functions
    @property
    def mass(self):
        return self._mass
    
    @property
    def position(self):
        return self._pos
    
    @property
    def getVelocity(self):
        return self._vel
    
    @property
    def getObjectRad(self):
        return self._coreDist
    
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

        # If for some reason the distance between the two objects is zero this will preven a divide by zero error
        if MagPos == 0:
            return np.array([0, 0, 0], dtype=np.float64)

        # Unit vector of position
        unitV = (otherObject.position - self.pos) / MagPos

        # Calculate acceleration due to gravity
        a = -(self.G * otherObject.mass) / (MagPos**2)

        return a * unitV
    
    # Distance between two objects
    def distance(self, otherObject):
        diff = self.pos - otherObject.getPosition()
        return np.linalg.norm(diff)