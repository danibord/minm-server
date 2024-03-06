import copy
import time
import numpy as np
from ODE import ODELibrary
from ODE.ode_system import ODESystem
from .kinetics_input_data import KineticsInputData
from .kinetics_output_data import KineticsOutputData
from django.http import JsonResponse

# Формирование массива результатов численного решения в экспериментальных точках
def calculate_numerical_solution_at_experimental_points(experimental_data, numerical_ODE_solution, time_array):
    calculations_at_experimental_points = copy.deepcopy(experimental_data)
    if len(time_array) != len(numerical_ODE_solution):
        return experimental_data
    for i in range(len(time_array)):
        for j in range(len(experimental_data)):
            if experimental_data[j][0] == time_array[i]:
                calculations_at_experimental_points[j][1:] = numerical_ODE_solution[i]
    return calculations_at_experimental_points

# Расчет ошибки вычислений в экспериментальных точках
def calculate_errors_at_experimental_points(experimental_data, numerical_ODE_solution):
    errors_at_experimental_points = copy.deepcopy(experimental_data)
    for i in range(len(experimental_data)):
        for j in range(1, len(experimental_data[i])):
            if experimental_data[i][j] == 0:
                errors_at_experimental_points[i][j] = 0
            else:
                errors_at_experimental_points[i][j] = np.round(((abs(experimental_data[i][j] - numerical_ODE_solution[i][j])) / experimental_data[i][j]) * 100, 5)
    return errors_at_experimental_points

# Решение системы ОДУ кинетических уравнений хим. реакции
# kinetics_input_data - разложенная по полям информация из JSON файла
def solve_kinetics_ode(kientics_input_data_from_json):
    kinetics_input_data =  KineticsInputData(kientics_input_data_from_json)
    stoichiometric_coefficients_matrix = kinetics_input_data.stoichiometric_coefficients_matrix
    exponents_of_substances_matrix = kinetics_input_data.exponents_of_substances_matrix
    experimental_data_matrix  = kinetics_input_data.experimental_data_matrix
    reaction_rate_constants = kinetics_input_data.reaction_rate_constants
    initial_time = kinetics_input_data.initial_time
    modeling_time = kinetics_input_data.modeling_time
    time_step = kinetics_input_data.time_step
    ODE_method_name = kinetics_input_data.ODE_method_name

    # Подготовка данных для расчета
    y0 = experimental_data_matrix[0][1:]
    time_array = np.linspace(initial_time, modeling_time, int((modeling_time - initial_time) / time_step) + 1)
    time_array = [round(x, 6) for x in time_array]
    system = ODESystem(y0, stoichiometric_coefficients_matrix, exponents_of_substances_matrix, reaction_rate_constants)
    lib = ODELibrary(system, ODE_method_name)

    # Численное решение системы ОДУ химических реакий
    calculation_start_time = time.time()
    kinetics_ODE_solution = lib.solve(time_array, y0)
    calculation_time = round(time.time() - calculation_start_time, 5)
    
    # Округление результатов до необходимой точности
    kinetics_ODE_solution = np.round(kinetics_ODE_solution, 3)
    time_array = np.round(time_array, 2)

    return kinetics_ODE_solution, kinetics_input_data, time_array, calculation_time

# Главный метод модуля, выполняет вычисления и отправляет данные обратно на клиент
def kinetics_solver_module_solution(kinetics_input_data_from_json):

    # Решение ОДУ системы хим.реакций
    kinetics_ODE_solution, kinetics_input_data, time_array, calculation_time = solve_kinetics_ode(kinetics_input_data_from_json)

    experimental_data = kinetics_input_data.experimental_data_matrix
    # Вычисление численных значений в экспериментальных точках
    numerical_solutions_at_experimental_points = calculate_numerical_solution_at_experimental_points(experimental_data,
                                                                                                     kinetics_ODE_solution,
                                                                                                     time_array)

    # Расчет погрешности вычислений в экспериментальных точках
    numerical_errors_at_experimental_points = calculate_errors_at_experimental_points(experimental_data, 
                                                                                      numerical_solutions_at_experimental_points)

    # Формирование объекта (делается для того, чтобы преобразование данных в корректный json файл было автоматическим)
    kinetics_output_data = KineticsOutputData(kinetics_ODE_solution,
                                              time_array, numerical_solutions_at_experimental_points,
                                              numerical_errors_at_experimental_points, calculation_time)
    
    # Отправка выходных данных на клиент в виде json файла
    return JsonResponse(kinetics_output_data.__dict__)