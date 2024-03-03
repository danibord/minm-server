import json

# test_kinetics_data.json - файл с примером входных данных
# Зона констант, которые хронят имена полей JSON файла
STOICHIOMETRIC_COEFFICIENTS_MATRIX = "stoichiometric_coefficients_matrix"
EXPONENTS_OF_SUBTANCES_MATRIX = "exponents_of_substances_matrix"
EXPERIMENTAL_DATA_MATRIX = "experimental_data_matrix"
REACTION_RATE_CONSTANTS = "reaction_rate_constants"
INITIAL_TIME = "initial_time"
MODELING_TIME = "modeling_time"
TIME_STEP = "time_step"
ODE_METHOD_NAME = "ODE_method_name"


# Обертка - обработка запроса от клиента.
# Принимает на вход функцию, в которую подает уже распаршенные из JSON данные
def with_request_data(function):
    def wrap_function(request):
        requestData = json.loads(request.body)
        return function(requestData)
    return wrap_function

def set_json_from_data(data):
    return json.dumps(data)