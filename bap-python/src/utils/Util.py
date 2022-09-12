# **********************************************************
# * Author        : XXXXXX
# * Email         : X@XXX.com
# * Create time   : 2022/XX/XX X:XX AM
# * Filename      : Util
# * Description   :
# **********************************************************
from abc import ABCMeta
from abc import abstractmethod


class Solution(metaclass=ABCMeta):

    """ Abstract Solution class. """

    def __init__(self):
        self.obj_val = 0

    def __lt__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        pass

    @abstractmethod
    def export_to_file(self, file_name: str) -> None:
        pass


class ViaSolverInterface(metaclass=ABCMeta):

    """
    Interface for solving problem via solver (e.g. Gurobi). Some basic methods are defined by default.
    """

    @abstractmethod
    def declare_vars(self):
        pass

    @abstractmethod
    def set_objective(self):
        pass

    @abstractmethod
    def add_constraints(self):
        pass

    @abstractmethod
    def set_param(self):
        pass

    @abstractmethod
    def optimize(self):
        pass


class PricingAlgorithmInterface(metaclass=ABCMeta):

    """
    Interface for pricing algorithm. Some basic methods are defined by default.
    """

    @abstractmethod
    def interrupt(self):
        pass

    @abstractmethod
    def _revise_cost_map(self, dist_map: dict, dual_val: list):
        pass

    @abstractmethod
    def solve(self, dist_map: dict, dual_val: list):
        pass


class HeuristicAlgorithmInterface(metaclass=ABCMeta):

    """ Interface for heuristic algorithm. Some basic methods are defined by default. """

    @abstractmethod
    def search(self):
        pass
