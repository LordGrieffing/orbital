import math



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
    
    
    # Sattelite Starting position vecotr
    Pos = [8377992.206, 0, 0]
    # Sattelite Starting velocity vector
    Vel = [0, 7120, 0]

    # Unit vector temp variable
    unitV = [0,0,0]
    
    # Calculate the orbit of the sattelite

    for i in range(1000):

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

        print(f"t: {i} Position: {Pos} Velocity: {Vel}")


if __name__ == "__main__":
    main()
