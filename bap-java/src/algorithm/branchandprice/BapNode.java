package algorithm.branchandprice;

import model.Solution;

import java.util.List;
import java.util.Map;

public abstract class BapNode implements Comparable<BapNode> {

    private boolean isIntegral;
    private int iteration;
    private double nodeObjectiveVal;
    private Solution solution;
    private boolean isLPFeasible;
    private BapNode parent;
    private Arc branchArc;
    private int nodeID;
    private Map<Record, Double> distMap;  // to store the distance map for inheritance
    private List<Integer> infeasiblePathIndices;

    /**
     * Column Generation process.
     *
     * @param rmp Restricted Master Problem.
     * @param sp Pricing sub Problem.
     */
    public void columnGeneration(RestrictedMasterProblem rmp, PricingProblem sp) {

    }

    /**
     * Update the feasible path indices in rmp after branching.
     *
     * @param rmp Restricted Master Problem
     */
    protected abstract void updateInfeasiblePath(RestrictedMasterProblem rmp);

    /**
     * Resolve distance map on graph after branching.
     */
    protected abstract void resolveGraph();

    @Override
    public int compareTo(BapNode bapNode) {
        if (nodeObjectiveVal <= bapNode.nodeObjectiveVal) {
            return -1;
        } else {
            return 1;
        }
    }
}
