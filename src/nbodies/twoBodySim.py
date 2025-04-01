import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import bodies as body


def main():
    
    # Mass of the Earth
    mE = 5.97219 * 10**24
    # Mass of the Sattelite
    mS = 10
    # Distance from the core of the earth to its surface
    coreDist = 6377992.206
    # Distance from surface to orbit
    surfaceDist = 2000000
    # Satelitte radius
    satRad = 5
    
    
    # start Positions
    posE = np.array([0, 0, 0], dtype=np.float64)
    posS = np.array([coreDist + surfaceDist, 0, 0], dtype=np.float64)

    # start velocitys
    velE = np.array([0, 0, 0], dtype=np.float64)
    velS = np.array([0, 7210 , 0], dtype=np.float64)


    # Create mass objects
    earth = body.massObject(mE, posE, velE, coreDist)
    satellite = body.massObject(mS, posS, velS, satRad)


    # variables to hold positions
    earthPath = []
    satellitePath = []

    # steps
    num_steps = 1000

    # difference in time
    dt = 30


    for i in range(num_steps):
        
        # Record current position
        earthPath.append(earth.position)
        satellitePath.append(satellite.position)

        # Calculate k constants
        














































if __name__ == "__main__":
    main()