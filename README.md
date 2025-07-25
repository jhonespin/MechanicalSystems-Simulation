## Projectile Motion with and without Air Friction

In common textbooks, parabolic motion is often studied without considering air friction.  
But how is the motion affected when air resistance is present?

To show students the importance of air friction, we present this brief code example.  
As the literature suggests, air resistance can be modeled as a force proportional to the velocity and acts in the direction opposite to motion.

This code was inspired by the following video:  
[https://www.youtube.com/watch?v=b9S_L1AaJNs](https://www.youtube.com/watch?v=b9S_L1AaJNs)

The solution of the resulting First Order Differential Equation (FODE) was assisted by [ChatGPT](https://chat.openai.com),  
where the model helped in debugging, commenting, and improving the structure of the Python code.

We used the `scipy.integrate` package from Python to simulate the system.

