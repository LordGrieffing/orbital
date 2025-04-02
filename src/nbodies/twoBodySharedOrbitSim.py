import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import bodies as body


def main():
    
    # Mass of the object1
    m1 = 1* 10**15
    # Mass of the Sattelite
    m2 = 1* 10**15
    # Distance from the core of the object1 to its surface
    coreDist1 = 10
    # Distance from surface to orbit
    surfaceDist = 2000000
    # Satelitte radius
    coreDist2 = 10
    
    
    # start Positions
    pos1 = np.array([500, 0, 0], dtype=np.float64)
    pos2 = np.array([-500, 0, 0], dtype=np.float64)

    # start velocitys
    vel1 = np.array([0, 7, 0], dtype=np.float64)
    vel2 = np.array([0, -7 , 0], dtype=np.float64)


    # Create mass objects
    object1 = body.massObject(m1, pos1, vel1, coreDist1)
    object2 = body.massObject(m2, pos2, vel2, coreDist2)


    # variables to hold positions
    object1Path = []
    object2Path = []

    # k constants for RungaKutta calculation
    object1KVel = np.zeros((4,3))
    object1KPos = np.zeros((4,3))
    object2KVel = np.zeros((4,3))
    object2KPos = np.zeros((4,3))

    # Object list
    objects = [object1, object2]

    # steps
    num_steps = 3000

    # difference in time
    dt = 1


    for i in range(num_steps):
        
        # Record current position
        object1Path.append(object1.position)
        object2Path.append(object2.position)

        #print(object2Path[i])

        # Calculate k constants
        object1KVel, object1KPos = object1.kUpdate(objects, dt)
        object2KVel, object2KPos = object2.kUpdate(objects, dt)

        # Update position and velocity of objects
        object1.posVelUpdate(object1KVel, object1KPos, dt)
        object2.posVelUpdate(object2KVel, object2KPos, dt)

    # Convert lists to arrays for plotting
    object1Path = np.array(object1Path)
    object2Path = np.array(object2Path)

    # Generate graph to show the orbits
    fig = plt.figure()
    axis = fig.add_subplot(111, projection='3d')

    # Scatter plot for object1 and object2
    object1_sc = axis.scatter([], [], [], color='blue', label="object1")
    object2_sc = axis.scatter([], [], [], color='red', label="object2")

    axis.set_xlim3d(-1500, 1500)
    axis.set_ylim3d(-1500, 1500)
    axis.set_zlim3d(-1500, 1500)


    # Animation update function
    def update(frame, sat_sc, object1_sc, object2Path, object1Path):
        sat_sc._offsets3d = (object2Path[:frame, 0], object2Path[:frame, 1], object2Path[:frame, 2])
        object1_sc._offsets3d = (object1Path[:frame, 0], object1Path[:frame, 1], object1Path[:frame, 2])
        return sat_sc, object1_sc

    # Run animation
    ani = FuncAnimation(fig, update, frames=num_steps, fargs=(object2_sc, object1_sc, object2Path, object1Path), interval=30)

    '''
    writer = PillowWriter(fps=15,
                                 metadata=dict(artist='Me'),
                                 bitrate=1800)
    ani.save("two_body_dance.gif", writer=writer)
    '''


    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()