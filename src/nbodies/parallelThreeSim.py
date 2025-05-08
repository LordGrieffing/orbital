import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import bodies as body
import random as rd
import threading

def main():
    # mass Scale factor
    massS = 11

    # Mass of objects
    m1 = 1* 10**massS
    m2 = 1* 10**massS
    m3 = 1* 10**massS

    # Radius of objects
    coreDist1 = 10
    coreDist2 = 10
    coreDist3 = 10
    
    
    # start Positions
    pos1 = np.array([0, 10, 0], dtype=np.float64)
    pos2 = np.array([0, -10, 0], dtype=np.float64)
    pos3 = np.array([0, 0, 0], dtype=np.float64)

    # start velocitys
    vel1 = np.array([0.2554309326049807, 0.516385834327506, 0], dtype=np.float64) * -1
    vel2 = np.array([0.2554309326049807, 0.516385834327506, 0], dtype=np.float64) * 1
    vel3 = np.array([0.2554309326049807, 0.516385834327506, 0], dtype=np.float64) * 1



    # Create mass objects
    object1 = body.massObject(m1, pos1, vel1, coreDist1)
    object2 = body.massObject(m2, pos2, vel2, coreDist2)
    object3 = body.massObject(m3, pos3, vel3, coreDist3)


    # variables to hold positions
    object1Path = []
    object2Path = []
    object3Path = []

    # k constants for RungaKutta calculation
    object1KVel = np.zeros((4,3))
    object1KPos = np.zeros((4,3))
    object2KVel = np.zeros((4,3))
    object2KPos = np.zeros((4,3))
    object3KVel = np.zeros((4,3))
    object3KPos = np.zeros((4,3))

    # Object list
    objects = [object1, object2, object3]

    # steps
    num_steps = 6000

    # difference in time
    dt = 1

    # Create threads
    t1 = threading.Thread()


    for i in range(num_steps):
        
        # Record current position
        object1Path.append(object1.position)
        object2Path.append(object2.position)
        object3Path.append(object3.position)

        #print(object2Path[i])

        # Calculate k constants
        object1KVel, object1KPos = object1.kUpdate(objects, dt)
        object2KVel, object2KPos = object2.kUpdate(objects, dt)
        object3KVel, object3KPos = object3.kUpdate(objects, dt)


        # Update position and velocity of objects
        object1.posVelUpdate(object1KVel, object1KPos, dt)
        object2.posVelUpdate(object2KVel, object2KPos, dt)
        object3.posVelUpdate(object3KVel, object3KPos, dt)

    # Convert lists to arrays for plotting
    object1Path = np.array(object1Path)
    object2Path = np.array(object2Path)
    object3Path = np.array(object3Path)

    # Generate graph to show the orbits
    fig = plt.figure()
    axis = fig.add_subplot(111, projection='3d')

    # Turning axis off
    #axis.set_axis_off()
    axis.legend().set_visible(False)

    # Scatter plot for object1 and object2
    object1_sc = axis.scatter([], [], [], color='blue', label="object1")
    object2_sc = axis.scatter([], [], [], color='red', label="object2")
    object3_sc = axis.scatter([], [], [], color='green', label="object3")

    axis.set_xlim3d(-15, 15)
    axis.set_ylim3d(-15, 15)
    axis.set_zlim3d(-15, 15)


    # Animation update function
    def update(frame, object3_sc, object2_sc, object1_sc, object3Path, object2Path, object1Path):
        object3_sc._offsets3d = (object3Path[:frame, 0], object3Path[:frame, 1], object3Path[:frame, 2])
        object2_sc._offsets3d = (object2Path[:frame, 0], object2Path[:frame, 1], object2Path[:frame, 2])
        object1_sc._offsets3d = (object1Path[:frame, 0], object1Path[:frame, 1], object1Path[:frame, 2])
        return object3_sc, object2_sc, object1_sc

    # Run animation
    ani = FuncAnimation(fig, update, frames=num_steps, fargs=(object3_sc, object2_sc, object1_sc, object3Path, object2Path, object1Path), interval=30)

    
    '''
    writer = PillowWriter(fps=25,
                                 metadata=dict(artist='Me'),
                                 bitrate=1800)
    ani.save("three_body_sample_3.gif", writer=writer)
    '''
    
    
    
    


    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
