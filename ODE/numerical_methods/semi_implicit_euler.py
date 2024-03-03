from copy import copy

import numpy as np

from ODE.numerical_methods import ExplicitEulerMethod
from ODE.ode_solver import ODESolver


class SemiImplicitEuler(ODESolver):
    def solve(self, time_array, y0):
        y_euler = ExplicitEulerMethod(self.system).solve(time_array, y0)
        dt = time_array[1] - time_array[0]
        y = copy(y0)
        y_next = copy(y0)
        solution = [y0]
        for i, t in enumerate(time_array[1:]):
            # Явная схема
            k = dt * self.system.func(y, t)
            #Полунеявня схема
            y = y + dt/2 * (self.system.func(y, t) + self.system.func(y_euler[i+1], t))
            y0 = copy(y)
            solution.append(y0)
        return np.array(solution)