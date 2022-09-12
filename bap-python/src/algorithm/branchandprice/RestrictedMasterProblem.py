# **********************************************************
# * Author        : XXXXXX
# * Email         : X@XXX.com
# * Create time   : 2022/XX/XX X:XX AM
# * Filename      : RestrictedMasterProblem
# * Description   :
# **********************************************************
from src.utils.Util import Solution


class RestrictedMasterProblem:

    """ Restricted Master Problem (RMP) class. """

    def __init__(self):
        self.model = None
        self.obj_val = 0
        self.is_integral = False
        self.column_list = []
        self.dual_val = []

    def init_model(self, init_cols: list) -> None:
        """ Initialize model. """
        pass

    def add_column(self, column_list: list) -> None:
        """ Add column or columns to RMP. """
        pass

    def optimize(self) -> bool:
        """ Optimize RMP, and return whether feasible. """

    def get_solution(self) -> Solution:
        """ Get solution if the linear relaxation of RMP is integral. """
        pass

    def _set_lp_solver_param(self) -> None:
        """ Set parameters of LP solver, e.g. turn off pre-solve and output. """
        pass




