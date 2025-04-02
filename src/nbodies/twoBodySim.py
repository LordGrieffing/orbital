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

    # k constants for RungaKutta calculation
    earthKVel = np.zeros((4,3))
    earthKPos = np.zeros((4,3))
    satelliteKVel = np.zeros((4,3))
    satelliteKPos = np.zeros((4,3))

    # steps
    num_steps = 1000

    # difference in time
    dt = 30


    for i in range(num_steps):
        
        # Record current position
        earthPath.append(earth.position)
        satellitePath.append(satellite.position)

        #print(satellitePath[i])

        # Calculate k constants
        earthKVel, earthKPos = earth.kUpdate(satellite, dt)
        satelliteKVel, satelliteKPos = satellite.kUpdate(earth, dt)

        # Update position and velocity of objects
        earth.posVelUpdate(earthKVel, earthKPos, dt)
        satellite.posVelUpdate(satelliteKVel, satelliteKPos, dt)

    # Convert lists to arrays for plotting
    earthPath = np.array(earthPath)
    satellitePath = np.array(satellitePath)

    # Generate graph to show the orbits
    fig = plt.figure()
    axis = fig.add_subplot(111, projection='3d')

    # Scatter plot for Earth and Satellite
    earth_sc = axis.scatter([], [], [], color='blue', label="Earth")
    sat_sc = axis.scatter([], [], [], color='red', label="Satellite")

    axis.set_xlim3d(-15000000, 15000000)
    axis.set_ylim3d(-15000000, 15000000)
    axis.set_zlim3d(-15000000, 15000000)


    # Animation update function
    def update(frame, sat_sc, earth_sc, satellitePath, earthPath):
        sat_sc._offsets3d = (satellitePath[:frame, 0], satellitePath[:frame, 1], satellitePath[:frame, 2])
        earth_sc._offsets3d = (earthPath[:frame, 0], earthPath[:frame, 1], earthPath[:frame, 2])
        return sat_sc, earth_sc

    # Run animation
    ani = FuncAnimation(fig, update, frames=num_steps, fargs=(sat_sc, earth_sc, satellitePath, earthPath), interval=30)

    plt.legend()
    plt.show()












































if __name__ == "__main__":
    main()