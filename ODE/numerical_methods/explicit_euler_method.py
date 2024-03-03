from copy import copy

import numpy as np

from ODE.ode_solver import ODESolver


class ExplicitEulerMethod(ODESolver):
    def solve(self, time_array, y0):
        print(time_array)
        dt = time_array[1] - time_array[0]
        y = copy(y0)
        solution = [y0]
        for t in time_array[1:]:
            #Явная схема
            k = dt * self.system.func(y, t)
            y += k
            y0 = copy(y)
            solution.append(y0)
        return np.array(solution)