# Orbital Mechanics
We can calculate orbits and motions of objects through space using simple differential equations.
In this repository I solve these equations in discret steps. This allows me to simulate different
oribatl paths between different objects.

# Euler vs Rungekutta
Euler's original method of solving these equations creates unstable orbits. We essentially get the
effect of gravity adding more acceleration than it should. The RungeKutta method allows us to 
average steps together and get a more accurate and smoother orbit. We can see this effect in these
two figures. The one on the left is using Euler's method the one on the right is using RungeKutta.

![alt text](https://github.com/LordGrieffing/orbital/blob/main/src/figures/satelitte_euler.gif) ![alt text](https://github.com/LordGrieffing/orbital/blob/main/src/figures/satelitte_RungeKutta.gif)