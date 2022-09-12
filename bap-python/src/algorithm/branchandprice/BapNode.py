# **********************************************************
# * Author        : XXXXXX
# * Email         : X@XXX.com
# * Create time   : 2022/XX/XX X:XX AM
# * Filename      : BapNode
# * Description   :
# **********************************************************
from src.algorithm.branchandprice.PricingProblem import PricingProblem
from src.algorithm.branchandprice.RestrictedMasterProblem import RestrictedMasterProblem


class BapNode:

    """ BapNode class for branch-and-bound procedure in Branch-and-Price algorithm. """

    def __init__(self):
        self.is_integral = False
        self.iteration = 0
        self.node_obj = float('inf')
        self.solution = None
        self.is_LP_feasible = True
        self.parent = None
        self.branch_arc = None
        self.node_id = 1
        self.dist_map = None
        self.infeasible_path_indices = None

    def __lt__(self, other):
        pass

    def column_generation(self, rmp: RestrictedMasterProblem, sp: PricingProblem) -> None:
        """
        Column Generation process.

        :param rmp: restricted master problem
        :param sp: pricing sub problem
        """
        pass

    def _update_feasible_path(self, rmp: RestrictedMasterProblem) -> None:
        """
        Update the feasible path set in rmp after branching.

        :param rmp: restricted master problem
        """
        pass

    def _resolve_graph(self) -> None:
        """ Resolve distance map on graph after branching. """
        pass

    def _get_history_branch_arcs(self) -> list:
        """
        Get history branch arcs list.

        :return: branching history list
        """
        pass
