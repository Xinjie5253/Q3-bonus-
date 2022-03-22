# We start by importing some necessary libraries (modules)
import numpy as np # this one is to do manipulate arrays 
import scipy as sp
import scipy.integrate as spi
import matplotlib.pyplot as plt
#  parameters configuration
dt=2
V=3
L=5
x0 = 0
y0 = 0
theta0 = np.deg2rad(5)
u=np.deg2rad(2)
a=np.tan(u)
#substituting t=0,x0=y0=0 and theta0 to attain the following formulas for C1,C2,C3


C3=theta0
C2=L*np.cos(theta0)/a
C1=-L*np.sin(theta0)/a

# form f(t, z)

def f(_t, z):
            # Define system dynamics 
            # [v*cos(θ), v*sin(θ), (v/L)*tan(u)]
            # z = (x, y, θ)
        theta=z[2]
        return [V*np.cos(theta),
                V*np.sin(theta),
                V*np.tan(np.deg2rad(2))/L]
sol = spi.solve_ivp(f, 
                    [0, dt],
                    [x0, y0,theta0], 
                    t_eval=np.linspace(0, dt, 2))
print(f"result from 'spicy' is : \n {sol.y}")
print('start analyse :\n')
print(f"C1={C1}, C2={C2}, C3={C3}")
theta=C3+V*(a*dt)/L
x=L*np.sin(theta)/a+C1
y=-L*np.cos(theta)/a+C2
print(f"result from analysis is : \n x = {x}, y = {y}, theta={theta}")

