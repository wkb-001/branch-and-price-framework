package algorithm.branchandprice;

import ilog.cplex.IloCplex;
import model.ProblemColumn;
import model.Solution;

import java.util.List;

public abstract class RestrictedMasterProblem {

    private IloCplex model;
    private double objectiveValue;
    private boolean isIntegral;
    private List<ProblemColumn> columnList;
    private List<Double> dualVal;

    /**
     * Initialize model.
     */
    public abstract void initModel();

    /**
     * Set Cplex Parameters.
     */
    public abstract void setLPSolverParam();

    /**
     * Add column or columns to RMP.
     */
    public abstract void addColumn();

    /**
     * Optimize RMP.
     *
     * @return whether RMP is feasible.
     */
    public abstract boolean optimize();

    /**
     * Get solution if the RMP is integral.
     */
    public abstract Solution getSolution();


}
