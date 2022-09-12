package algorithm.branchandprice;

import model.ProblemColumn;

public abstract class PricingProblem {

    ProblemColumn shortestPath;
    double reducedCost;

    protected abstract void reset();

}
