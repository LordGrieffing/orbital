import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np


def accelerate(Pos, G, mE):

    # Magnitute of position
    MagPos = np.linalg.norm(Pos)

    # Unit vector of position
    unitV = Pos / MagPos

    # Calculate acceleration due to gravity
    a = -(G * mE) / (MagPos**2)

    #print(a * unitV)
    return a * unitV

def main():
    
    # Gravitational Constant
    G = 6.674 * 10**-11
    # Mass of the Earth
    mE = 5.97219 * 10**24
    # Mass of the Sattelite
    mS = 10
    # Distance from the core of the earth to its surface
    coreDist = 6377992.206
    # Distance from surface to orbit
    surfaceDist = 2000000

    # Lists to store position data for plotting
    x_vals, y_vals, z_vals = [], [], []

    # Define number of steps
    num_steps = 50000

    # Define change in time. Higher numbers run faster but less accurate
    dt = 30
    
    
    # Sattelite Starting position vector
    Pos = np.array([coreDist + surfaceDist, 0, 0], dtype=np.float64)
    # Sattelite Starting velocity vector
    Vel = np.array([0, 7210 , 0], dtype=np.float64)

    # Constant arrays
    kPos = np.zeros((4,3))
    kVel = np.zeros((4,3))
    
    # Calculate the orbit of the sattelite

    for i in range(num_steps):

        # Store current position for visualization
        x_vals.append(Pos[0])
        y_vals.append(Pos[1])
        z_vals.append(Pos[2])

        # Calculate Position Constants

        # Calculate k1
        kVel[0] =  accelerate(Pos, G, mE)
        kPos[0] = Vel

        # Calculate k2
        kVel[1] =  accelerate(Pos + (0.5 * kPos[0])*dt, G, mE)
        kPos[1] = Vel + 0.5 * kVel[0] * dt

        # Calculate k3
        kVel[2] =  accelerate(Pos + (0.5 * kPos[1])*dt, G, mE)
        kPos[2] = Vel + 0.5 * kVel[1] * dt

        # Calculate k4
        kVel[3] =  accelerate(Pos + (kPos[2])*dt, G, mE)
        kPos[3] = Vel + kVel[2] * dt

        # Update the positions of the orbit
        Vel = Vel + (dt /6) * (kVel[0] + 2*kVel[1] + 2*kVel[2] + kVel[3])
        Pos = Pos + (dt /6) * (kPos[0] + 2*kPos[1] + 2*kPos[2] + kPos[3])

        #print(f"t: {i} Position: {Pos} Velocity: {Vel}")


   
    fig = plt.figure()
    axis = fig.add_subplot(111, projection='3d')

    # Generate Earth
    axis.scatter(0, 0, 0, color="red", s=200, label="Earth")

    axis.set_xlim3d(min(x_vals), max(x_vals))
    axis.set_ylim3d(min(y_vals), max(y_vals))
    axis.set_zlim3d(min(y_vals), max(y_vals))

    animated_plot, = axis.plot([], [], [])
    
    # Frame updating function
    def update_frame(frame):

        # Set orbit data
        # Define the x, y values
        animated_plot.set_data(x_vals[:frame], y_vals[:frame])
        # Define the z values
        animated_plot.set_3d_properties(z_vals[:frame])
        
        return animated_plot, 




    # Animate the graph
    ani= FuncAnimation(
        
                fig = fig,
                func= update_frame,
                frames= num_steps,
                interval=2,
                )

    
    # Save satelitte_animation
    writer = PillowWriter(fps=15,
                                 metadata=dict(artist='Me'),
                                 bitrate=1800)
    ani.save("satelitte_animation_euler.gif", writer=writer)
    
    plt.show()


if __name__ == "__main__":
    main()