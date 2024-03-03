import json
from reaction_kinetics_solver_module.kinetics_input_data import KineticsInputData

class KineticsOutputData():
    def __init__(self, kinetics_ODE_solution,
                       time_array,
                       numerical_solutions_at_experimental_points,
                       numerical_errors_at_experimental_points,
                       calculation_time):
                
                self.kinetics_ODE_solution = kinetics_ODE_solution.tolist()
                self.time_array = time_array.tolist()
                self.numerical_solutions_at_experimental_points = numerical_solutions_at_experimental_points
                self.numerical_errors_at_experimental_points = numerical_errors_at_experimental_points
                self.calculation_time = calculation_time