import math
import matplotlib.pyplot as plt



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
    
    
    # Sattelite Starting position vecotr
    Pos = [8377992.206, 0, 0]
    # Sattelite Starting velocity vector
    Vel = [0, 6800 , 0]

    # Unit vector temp variable
    unitV = [0,0,0]
    
    # Calculate the orbit of the sattelite

    for i in range(50000):

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
            Pos[j] = Pos[j] + Vel[j]

        # Calculate New Velocity vector
        for j in range(3):
            Vel[j] = Vel[j] + (a * unitV[j])

    # Plot the orbit
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot satellite trajectory
    ax.plot(x_vals, y_vals, z_vals, label="Satellite Orbit", color="blue")

    # Plot Earth (as a point)
    ax.scatter(0, 0, 0, color="red", s=100, label="Earth")

    # Labels and legend
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")
    ax.set_zlabel("Z Position (m)")
    ax.legend()
    plt.show()




if __name__ == "__main__":
    main()