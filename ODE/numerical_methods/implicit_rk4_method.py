from copy import copy

import numpy as np

from ODE.numerical_methods import ExplicitEulerMethod
from ODE.ode_solver import ODESolver


class ImplicitRK4Method(ODESolver):
    def solve(self, time_array, y0):
        y_euler = ExplicitEulerMethod(self.system).solve(time_array, y0)
        dt = time_array[1] - time_array[0]
        y = copy(y0)
        solution = [y0]
        for i, t in enumerate(time_array[1:]):
            # Неявная схема для k1,k2,k3,k4 с помощью метода Эйлера
            k1 = self.system.func(y_euler[i+1], t)
            k2 = self.system.func(y_euler[i+1] + dt/2*k1, t + dt/2)
            k3 = self.system.func(y_euler[i+1] + dt/2*k2, t + dt/2)
            k4 = self.system.func(y_euler[i+1] + dt*k3, t + dt)
            k = dt/6 * (k1 + 2*k2 + 2*k3 + k4)
            y += k
            y0 = copy(y)
            solution.append(y0)
        return np.array(solution)