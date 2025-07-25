# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 12:39:36 2025

@author: Jhon Jairo ESpinosa
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros
B = 1
V = 5
theta = np.radians(40)
g = 9.8

# Tiempo de vuelo sin fricción (analítico)
T_flight = 2 * V * np.sin(theta) / g
x_max = (V**2) * np.sin(2 * theta) / g

# Para estar seguros, extendemos un poco más el rango
t_eval = np.linspace(0, T_flight * 1.1, 200)
x_ideal = np.linspace(0, x_max * 1.1, 200)

# Ecuación con fricción
def dSdt(t, S, B):
    x, vx, y, vy = S
    v = np.sqrt(vx**2 + vy**2)
    return [vx, -B * v * vx, vy, -g - B * v * vy]

# Condiciones iniciales
y0 = [0, V * np.cos(theta), 0, V * np.sin(theta)]

# Solución numérica con fricción
sol = solve_ivp(dSdt, [0, t_eval[-1]], y0, t_eval=t_eval, args=(B,))

# Solución analítica sin fricción
y_ideal = np.tan(theta) * x_ideal - (g / (2 * (V * np.cos(theta))**2)) * x_ideal**2

# Filtramos solo valores positivos de y (en caso de que haya caída por debajo del suelo)
mask = sol.y[2] >= 0

# Gráfica
plt.figure(figsize=(8,6))
plt.plot(x_ideal, y_ideal, label='Sin fricción (ideal)', color='purple')
plt.plot(sol.y[0][mask], sol.y[2][mask], label='Con fricción (B=1)', color='orange')
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.title('Comparación: Movimiento Parabólico con y sin Fricción', fontsize=16)
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)
plt.xlim(left=0)
plt.show()
