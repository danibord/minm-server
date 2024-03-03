import numpy as np

from ODE.numerical_methods.explicit_euler_method import ExplicitEulerMethod
from ODE.numerical_methods.explicit_rk2_method import ExplicitRK2Method
from ODE.numerical_methods.explicit_rk4_method import ExplicitRK4Method 
from ODE.numerical_methods.explicit_second_adams import ExplicitAdams2Method
from ODE.numerical_methods.trapezoid_method import TrapezoidMethod
from ODE.numerical_methods.middle_poind_method import MiddlePointMethod 
from ODE.numerical_methods.km_method import KuttaMersonMethod 
from ODE.numerical_methods.implicit_euler_method import ImplicitEulerMethod
from ODE.numerical_methods.implicit_rk4_method import ImplicitRK4Method
from ODE.numerical_methods.implicit_rk2_method import ImplicitRK2Method
from ODE.numerical_methods.semi_implicit_euler import SemiImplicitEuler 
from ODE.numerical_methods.semi_implicit_rk2 import SemiImplicitRK2Method
from ODE.numerical_methods.semi_implicit_rk4 import SemiImplicitRK4Method

EXPLICIT_EULER = 'EXPLICIT_EULER'
IMPLICIT_EULER = 'IMPLICIT_EULER'
SEMI_IMPLICIT_EULER = 'SEMI_IMPLICIT_EULER'
EXPLICIT_RK2 = 'EXPLICIT_RK2'
IMPLICIT_RK2 = 'IMPLICIT_RK2'
SEMI_IMPLICIT_RK2 = 'SEMI_IMPLICIT_RK2'
EXPLICIT_RK4 = 'EXPLICIT_RK4'
IMPLICIT_RK4 = 'IMPLICIT_RK4'
SEMI_IMPLICIT_RK4 = 'SEMI_IMPLICIT_RK4'
TRAPEZOID = 'TRAPEZOID'
MIDDLE_POINT = 'MIDDLE_POINT'
KUTTA_MERSON = 'KUTTA_MERSON'
EXPLICIT_2STEP_ADAMS = 'EXPLICIT_2STEP_ADAMS'

class ODELibrary:
    def __init__(self, ODE_system, method_name, accuracy = 6):
        """
        Инициализация библиотеки для выбора метода решения системы оду.

        Parameters:
        - ODE_system: система оду хим. рекции
        - method_name: имя метода решения
        - accuracy: число значимых знаков после запятой
        """
        self.ODE_system = ODE_system
        self.method_name = method_name
        self.accuracy = accuracy

    def solve(self, time_array, y0):
        solution = None

        if self.method_name == EXPLICIT_EULER:
            solution = ExplicitEulerMethod(self.ODE_system).solve(time_array, y0)
        if self.method_name == IMPLICIT_EULER:
            solution = ImplicitEulerMethod(self.ODE_system).solve(time_array, y0)
        if self.method_name == SEMI_IMPLICIT_EULER:
            solution = SemiImplicitEuler(self.ODE_system).solve(time_array, y0)
        if self.method_name == EXPLICIT_RK2:
            solution = ExplicitRK2Method(self.ODE_system).solve(time_array, y0)
        if self.method_name == IMPLICIT_RK2:
            solution = ImplicitRK2Method(self.ODE_system).solve(time_array, y0)
        if self.method_name == SEMI_IMPLICIT_RK2:
            solution = SemiImplicitRK2Method(self.ODE_system).solve(time_array, y0)
        if self.method_name == EXPLICIT_RK4:
            solution = ExplicitRK4Method(self.ODE_system).solve(time_array, y0)
        if self.method_name == IMPLICIT_RK4:
            solution = ImplicitRK4Method(self.ODE_system).solve(time_array, y0)
        if self.method_name == SEMI_IMPLICIT_RK4:
            solution = SemiImplicitRK4Method(self.ODE_system).solve(time_array, y0)
        if self.method_name == TRAPEZOID:
            solution = TrapezoidMethod(self.ODE_system).solve(time_array, y0)
        if self.method_name == MIDDLE_POINT:
            solution = MiddlePointMethod(self.ODE_system).solve(time_array, y0)
        if self.method_name == KUTTA_MERSON:
            solution = KuttaMersonMethod(self.ODE_system).solve(time_array, y0)
        if self.method_name == EXPLICIT_2STEP_ADAMS:
            solution = ExplicitAdams2Method(self.ODE_system).solve(time_array, y0)


        if solution is not None:
            return np.round(solution, self.accuracy)
        return solution