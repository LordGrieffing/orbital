import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import mpl_toolkits.mplot3d.axes3d as p3



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
    num_steps = 3000

    # Define change in time. Higher numbers run faster but less accurate
    dt = 30
    
    
    # Sattelite Starting position vecotr
    Pos = [coreDist + surfaceDist, 0, 0]
    # Sattelite Starting velocity vector
    Vel = [0, 7210 , 0]

    # Unit vector temp variable
    unitV = [0,0,0]
    
    # Calculate the orbit of the sattelite

    for i in range(num_steps):

        # Store current position for visualization
        x_vals.append(Pos[0])
        y_vals.append(Pos[1])
        z_vals.append(Pos[2])


        # Magnitute of position
        MagPos = math.sqrt(Pos[0]**2 + Pos[1]**2 + Pos[2]**2)

        # Unit vector of position
        for j in range(3):
            unitV[j] = Pos[j] / MagPos

        # Calculate acceleration due to gravity
        a = -(G * mE) / (MagPos**2)

        # Calculate New Position vector
        for j in range(3):
            Pos[j] = Pos[j] + Vel[j] * dt

        # Calculate New Velocity vector
        for j in range(3):
            Vel[j] = Vel[j] + (a * unitV[j]) * dt

    
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
    ani = FuncAnimation(
        
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