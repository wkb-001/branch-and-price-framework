# **********************************************************
# * Author        : XXXXXX
# * Email         : X@XXX.com
# * Create time   : 2022/XX/XX X:XX AM
# * Filename      : BapNode
# * Description   :
# **********************************************************
from src.algorithm.branchandprice.PricingProblem import PricingProblem
from src.algorithm.branchandprice.RestrictedMasterProblem import RestrictedMasterProblem
from src.utils.Util import Solution


class BapNode:

    """ BapNode class for branch-and-bound procedure in Branch-and-Price algorithm. """

    def __init__(self):
        self.is_integral: bool = False
        self.iteration: int = 0
        self.node_obj: float = float('inf')
        self.solution: Solution = None
        self.is_LP_feasible: bool = True
        self.parent: BapNode = None
        self.branch_arc: tuple = None
        self.node_id: int = 1
        self.dist_map: dict = None
        self.infeasible_path_indices: list = None

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
        Update the feasible path indices in rmp after branching.

        :param rmp: restricted master problem
        """
        pass

    def _resolve_graph(self) -> None:
        """ Resolve distance map on graph after branching. """
        pass
