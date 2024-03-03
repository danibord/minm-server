from copy import copy

import numpy as np

from ODE.numerical_methods import ExplicitEulerMethod
from ODE.ode_solver import ODESolver


class SemiImplicitRK2Method(ODESolver):
    def solve(self, time_array, y0):
        y_euler = ExplicitEulerMethod(self.system).solve(time_array, y0)
        dt = time_array[1] - time_array[0]
        y = copy(y0)
        solution = [y0]
        for i, t in enumerate(time_array[1:]):
            # Явная схема для k1
            k1 = self.system.func(y, t)
            # Неявная схема для k2
            k2 = self.system.func(y_euler[i + 1] + dt / 2 * k1, t + dt / 2)
            # Полунеяная схема для y_n+1
            k = dt * k2
            y += k
            y0 = copy(y)
            solution.append(y0)
        return np.array(solution)