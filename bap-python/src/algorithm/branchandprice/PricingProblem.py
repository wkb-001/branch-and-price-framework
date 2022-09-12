# **********************************************************
# * Author        : XXXXXX
# * Email         : X@XXX.com
# * Create time   : 2022/XX/XX X:XX AM
# * Filename      : PricingProblem
# * Description   :
# **********************************************************
class PricingProblem:

    """ Price problem class. """

    def __init__(self):
        self.shortest_path = None
        self.reduced_cost = float('inf')
        # as for the solution approach, heuristic pricing and other exact pricing algorithm can be used
        self.sol_approach = None

    def _reset(self):
        """ Reset shortest path as None, and reduced cost as infinity. """
        self.shortest_path = None
        self.reduced_cost = float('inf')

    def solve(self, dist_map: dict, dual_val: list) -> list:
        """ Solve pricing sub problem, and return all the negative reduced cost paths. """
        pass

