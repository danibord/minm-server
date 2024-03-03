from copy import copy

import numpy as np

from ODE.ode_solver import ODESolver


class KuttaMersonMethod(ODESolver):
    def solve(self, time_array, y0):
        dt = time_array[1] - time_array[0]
        y = copy(y0)
        solution = [y0]
        for t in time_array[1:]:
            k1 = dt * self.system.func(y, t)
            k2 = dt * self.system.func(y + k1 / 3, t + dt / 3)
            k3 = dt * self.system.func(y + k1 / 6 + k2 / 6, t + dt / 2)
            k4 = dt * self.system.func(y - k2 / 3 + k3, t + 2 * dt / 3)
            k5 = dt * self.system.func(y + k1 / 8 + 3 * k2 / 8 + 3 * k3 / 8 + k4 / 8, t + dt)
            y += (k1 / 6 + k2 / 3 + k3 / 3 + k4 / 6 + k5 / 6)
            y0 = copy(y)
            solution.append(y0)
        return np.array(solution)