from copy import copy

import numpy as np

from ODE.ode_solver import ODESolver


class ExplicitRK4Method(ODESolver):
    def solve(self, time_array, y0):
        dt = time_array[1] - time_array[0]
        y = copy(y0)
        solution = [y0]
        for t in time_array[1:]:
            k1 = self.system.func(y, t)
            k2 = self.system.func(y + dt/2*k1, t + dt/2)
            k3 = self.system.func(y + dt/2*k2, t + dt/2)
            k4 = self.system.func(y + dt*k3, t + dt)
            k = dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            y += k
            y0 = copy(y)
            solution.append(y0)
        return np.array(solution), time_array