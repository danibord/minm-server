from copy import copy

import numpy as np

from ODE.numerical_methods import ExplicitEulerMethod
from ODE.ode_solver import ODESolver


class ImplicitEulerMethod(ODESolver):
    def solve(self, time_array, y0):
        y_euler = ExplicitEulerMethod(self.system).solve(time_array, y0)
        dt = time_array[1] - time_array[0]
        y = copy(y0)
        solution = [y0]
        for i, t in enumerate(time_array[1:]):
            # Находим y_n+1 неявно с помощью явного метода Эйлера
            k = dt * self.system.func(y_euler[i + 1], t)
            y += k
            y0 = copy(y)
            solution.append(y0)
        return np.array(solution)