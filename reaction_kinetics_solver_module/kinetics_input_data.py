from utils.json_service import STOICHIOMETRIC_COEFFICIENTS_MATRIX, EXPONENTS_OF_SUBTANCES_MATRIX, \
                         EXPERIMENTAL_DATA_MATRIX, INITIAL_TIME, TIME_STEP, MODELING_TIME, \
                         REACTION_RATE_CONSTANTS, ODE_METHOD_NAME 


class KineticsInputData():
    def __init__(self, json_kinetics_data):
        #self.table_parameters = models.ForeignKey(TableParameters, on_delete=models.CASCADE, verbose_name="Параметры таблицы")
        self.initial_time = json_kinetics_data[INITIAL_TIME]
        self.modeling_time = json_kinetics_data[MODELING_TIME]
        self.time_step = json_kinetics_data[TIME_STEP]
        self.stoichiometric_coefficients_matrix = json_kinetics_data[STOICHIOMETRIC_COEFFICIENTS_MATRIX]
        self.exponents_of_substances_matrix = json_kinetics_data[EXPONENTS_OF_SUBTANCES_MATRIX]
        self.experimental_data_matrix = json_kinetics_data[EXPERIMENTAL_DATA_MATRIX]
        self.reaction_rate_constants = json_kinetics_data[REACTION_RATE_CONSTANTS] 
        self.ODE_method_name = json_kinetics_data[ODE_METHOD_NAME]