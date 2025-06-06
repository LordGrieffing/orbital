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
    def velocity(self):
        return self._vel
    
    @property
    def objectRad(self):
        return self._coreDist
    
    # Set mass object attribute functions
    def setPosition(self, position):
        self._pos = position

    def setVelocity(self, velocity):
        self._vel = velocity

    
    # Functions to handle physics and movement
    
    # Acceleration due to gravity function
    def accelerate(self, otherObject, offset = None):

        # Stash current position
        tempPos = self.position
        
        # if offset was provided update position for purpose of acceleration calculation
        if offset is not None:
            self.setPosition(self.position + offset)

        # Magnitute of distance
        MagPos = self.distance(otherObject)

        # If for some reason the distance between the two objects is zero this will preven a divide by zero error
        if MagPos == 0:
            return np.array([0, 0, 0], dtype=np.float64)
        
        # if an offset was provided use this for position

        # Unit vector of position
        #unitV = (otherObject.position - self.position) / MagPos
        unitV = (self.position - otherObject.position) / MagPos

        # Calculate acceleration due to gravity
        a = -(self.G * otherObject.mass) / (MagPos**2)

        # reset to previously stashed position
        self.setPosition(tempPos)

        return a * unitV
    
    # Test function to see if three or more bodies can work
    def accelerateN(self, objectsInfo, offset = None):

        temp_pos = self.position

        if offset is not None:
            self.setPosition(self.position + offset)

        total_acc = np.array([0.0,0.0,0.0], dtype=np.float64)

        for pos, vel, mass in objectsInfo:
            if not self.samePosition(temp_pos, pos):
                r_vec = self.position - pos
                r_mag = np.linalg.norm(r_vec)

                if r_mag == 0:
                    continue

                unitV = r_vec / r_mag
                a = -(self.G * mass) / (r_mag**2)

                total_acc += a * unitV

        self.setPosition(temp_pos)

        return total_acc
    
    # Distance between two objects
    def distance(self, otherObject):
        diff = self.position - otherObject.position
        return np.linalg.norm(diff)
    
    # Calculate k constants
    def kUpdate(self, ObjectsInfo, dt):
        kPos = np.zeros((4, 3))
        kVel = np.zeros((4, 3))

        # k1
        kVel[0] = self.accelerateN(ObjectsInfo)
        kPos[0] = self.velocity

        # k2
        kVel[1] = self.accelerateN(ObjectsInfo, (kPos[0]*0.5*dt))
        kPos[1] = self.velocity + 0.5*kVel[0]*dt

        # k3
        kVel[2] = self.accelerateN(ObjectsInfo, (kPos[1]*0.5*dt))
        kPos[2] = self.velocity + 0.5*kVel[1]*dt

        # k4
        kVel[3] = self.accelerateN(ObjectsInfo, (kPos[2]*dt))
        kPos[3] = self.velocity + kVel[2]*dt

        return kVel, kPos

    # update position and velocity
    def posVelUpdate(self, kVel, kPos, dt):
        
        # delta velocity and delta position
        dV = (dt /6) * (kVel[0] + 2*kVel[1] + 2*kVel[2] + kVel[3])
        dP = (dt /6) * (kPos[0] + 2*kPos[1] + 2*kPos[2] + kPos[3])
        
        # update position
        self.setPosition(self.position + dP)

        # update velocity
        self.setVelocity(self.velocity + dV)

    # Checks if two positions are the same position
    def samePosition(self, pos1, pos2):
        for i in range(len(pos1)):
            if pos1[i] != pos2[i]:
                return False
            
        return True