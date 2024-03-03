from abc import ABC, abstractmethod


class ODESolver(ABC):
    def __init__(self, system, decimal_place=6):
        """
        Абстрактный класс для численного решения ОДУ

        Parameters:
        - system: система ОДУ
        - decimal_place: параметр округления
        """
        self.system = system
        self.decimal_place = decimal_place


    @abstractmethod
    def solve(self, time_array, y0):
        """
         Абстрактный метод для численного решения системы ОДУ.

         Parameters:
        - time_array: массив времени
        - y0: начальные значения системы оду
        """
        pass