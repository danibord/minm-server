from copy import copy

import numpy as np

from ODE.ode_solver import ODESolver


class ExplicitAdams2Method(ODESolver):
    def solve(self, time_array, y0):
        dt = time_array[1] - time_array[0]
        y = copy(y0)
        solution = [y0]
        for i, t in enumerate(time_array[1:]):
            if i == 0:
                # Use Euler method to get second point
                y1 = y + dt * self.system.func(y, t)
                y0 = copy(y1)
                solution.append(y0)
                y = y1
            else:
                # Use Adams-Bashforth 2-step method
                y += dt/2 * (3*self.system.func(y, t) - self.system.func(y0, t-dt))
                y0 = copy(y)
                solution.append(y0)
        return np.array(solution)