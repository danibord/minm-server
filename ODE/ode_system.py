import numpy as np


class ODESystem():
    def __init__(self, y0, stoichiometric_coefficients_matrix, exponents_of_substances_matrix, reaction_rate_constants):
        self.y0 = y0
        self.stoichiometric_coefficients_matrix = stoichiometric_coefficients_matrix
        self.exponents_of_substances_matrix = exponents_of_substances_matrix
        self.reaction_rate_constants = reaction_rate_constants
        self.components = len(self.stoichiometric_coefficients_matrix[0])
        self.stages = len(self.stoichiometric_coefficients_matrix)

    def func(self, y, t):
        C = np.zeros(self.components)
        sumC = np.zeros(self.components)
        r = np.zeros(self.stages)
        sumR = np.zeros(self.stages)
        for i in range(self.stages):
            sumR[i] = self.reaction_rate_constants[i][0]
            for j in range(self.components):
                if self.exponents_of_substances_matrix[i][j] != -1:
                    r[i] = y[j] ** self.exponents_of_substances_matrix[i][j]
                    sumR[i] *= r[i]
        for i in range(self.components):
            for j in range(self.stages):
                C[i] = self.stoichiometric_coefficients_matrix[j][i] * sumR[j]
                sumC[i] += C[i]
        return sumC