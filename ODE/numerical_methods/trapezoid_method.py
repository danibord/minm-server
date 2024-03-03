from copy import copy

import numpy as np

from ODE.ode_solver import ODESolver


class TrapezoidMethod(ODESolver):
    def solve(self, time_array, y0):
        dt = time_array[1] - time_array[0]
        y = copy(y0)
        solution = [y0]
        for t in time_array[1:]:
            k1 = self.system.func(y, t)
            k2 = self.system.func(y + dt * k1, t + dt)
            y += dt / 2 * (k1 + k2)
            y0 = copy(y)
            solution.append(y0)
        return np.array(solution)