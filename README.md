# Orbital Mechanics
We can calculate orbits and motions of objects through space using simple differential equations.
In this repository I solve these equations in discret steps. This allows me to simulate different
oribatl paths between different objects.

# Euler vs Rungekutta
When I started this project I learned Euler's method fo calculating orbits first. It is simple which was 
good for me to learn the basic concept of how to update my position and velocity. However this simplicity 
leads to problems when it comes to accuracy of our calculations. In the figures below I am displaying the
same orbit of two bodys but using different methods to calculate their positions. On the Left I am using
Eulter's method. As we can see we get a spiraling effect where the satellite's orbit is gain extra 
acceleration with each transit.


<p>
    <img src="https://github.com/LordGrieffing/orbital/blob/main/src/figures/satelitte_euler.gif" width="45%" />
    <img src="https://github.com/LordGrieffing/orbital/blob/main/src/figures/satelitte_RungeKutta.gif" width="45%" />
</p>

This happens because Euler's method doesn't fully account for how dynamic the system is. As we progress
forward in time the affects of gravity are constantly changing. A method such as RungeKutta gives us
more stable and accurate orbits because it looks multiple steps ahead and averages these steps together.


# Three Bodies or More
Two bodies are great but what really shows off how crazy these mechanics can get is when we add in a third
body. Once we have three bodies the system becomes much more unstable. Not only do we lose the uniform 
motion that we see with just two bodies but also most system end up ejecting the bodies out. 

<p>
    <img src="https://github.com/LordGrieffing/orbital/blob/main/src/figures/three_body_mayhem.gif">
</p>

However even though there is no general solution for these dynamic systems as a whole. There are a number
of three body systems that, given the correct intial velocities and positions do have a "stable" existance.
Here is an example of what one these stable three body systems look.

<p>
    <img src="https://github.com/LordGrieffing/orbital/blob/main/src/figures/three_body_corkscrew.gif">
</p>