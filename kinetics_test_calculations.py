import json
from ODE import ode_library
from reaction_kinetics_solver_module.reaction_kinetics_solver import solve_kinetics_ode
import plotly.graph_objects as go
import plotly

def func():
# Реакция алкилирования фенилацетонитрила - тестовая реакция из диплома Ильи
    data_for_json_file = {
    "stoichiometric_coefficients_matrix": [
        [-1, -1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, -1, -1, -1, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, -1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, -1, -1, 0, 0],
        [0, -1, 0, 1, 1, 0, -1, 0, 1, 0],
        [0, 1, 0, -1, -1, 0, 1, 0, -1, 0],
        [0, 0, 0, 0, 0, -1, 0, 1, -1, 1],
        [0, 0, 0, 0, 0, 1, 0, -1, 1, -1]
    ],
    "exponents_of_substances_matrix": [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0 ,0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
    ],
    "experimental_data_matrix": [
        [0, 3.007, 16, 0, 0, 0, 3.233, 0, 0, 0, 0],
        [0.2, 2.587, 0, 0, 0, 0, 0, 0.229, 0, 0, 0.001],
        [0.5, 2.044, 0, 0, 0, 0, 0, 0.597, 0, 0, 0.005],
        [1, 1.925, 0, 0, 0, 0, 0, 0.839, 0, 0, 0.007],
        [2, 1.253, 0, 0, 0, 0, 0, 1.573, 0, 0, 0.03],
        [4, 0.835, 0, 0, 0, 0, 0, 2.12, 0, 0, 0.053]
    ],
    "reaction_rate_constants":[
        [0.671],
        [3.34],
        [4.3],
        [0.017],
        [0.78],
        [2.44],
        [0.88],
        [1.95]
    ],
    "initial_time": 0,
    "modeling_time": 60,
    "time_step": 0.1,
    "ODE_method_name": ode_library.IMPLICIT_RK2
    }

# все действия проделывать в visual studio code
# ctrl + shift + p => python create environment => venv => python 3.10
# закрыть terminal => открыть terminal => (ctrl + shift + ё) => pip install -r requirements.txt

    file_name = "test_kinetics_data.json"
    with open(file_name, 'w') as file:
        json.dump(data_for_json_file, file,  indent=4)

    json_file_imitation = json.dumps(data_for_json_file)

    kinetics_ODE_solution, kinetics_input_data, time_array, calculation_time = solve_kinetics_ode(json.loads(json_file_imitation))
    print(kinetics_ODE_solution)
    print(kinetics_ODE_solution.tolist())

    # Создание объекта для графика
    fig = go.Figure()

    # Построение графика
    for i in range(len(kinetics_ODE_solution[0])):
        y = [row[i] for row in kinetics_ODE_solution]
        fig.add_trace(go.Scatter(x=time_array, y=y, mode='lines', name=f'Концентрация {i+1}'))

    # Настройка графика
    fig.update_layout(title='График концентраций по времени', xaxis_title='Время', yaxis_title='Концентрация')

    # Отображение графика
    fig.show()


func()
print(plotly.__version__)