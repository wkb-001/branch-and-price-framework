package algorithm.branchandprice;

import model.Solution;

import java.util.PriorityQueue;

import static model.Parameter.MIP_SEARCH_GAP_TOL;

public abstract class BranchAndPrice {

    private boolean silent;
    private boolean optFlag;
    private RestrictedMasterProblem rmp;
    private PricingProblem sp;
    // solution information
    private int nodeExplored;
    private int totalCGIteration;
    private BapNode bestNode;
    private double mipSearchGap;
    private long cpuTime;
    private double lb;
    private double ub;
    private double rootRelaxationVal;
    private PriorityQueue<BapNode> queue;
    private PriorityQueue<Solution> solutionPool;

    /**
     * Print solution information.
     */
    public abstract void printSolution();

    public abstract boolean solve();
}
