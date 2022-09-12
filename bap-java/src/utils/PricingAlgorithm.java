package utils;

import java.util.List;
import java.util.Map;

public interface PricingAlgorithm {

    /**
     * Revise cost map in the Column Generation Process.
     *
     * @param distMap distance map on the graph
     * @param dualVal dual value list
     */
    void reviseCostMap(Map<Record, Double> distMap, List<Double> dualVal);

    /**
     * Solve Shortest Path Problem with Resource Constraints.
     *
     * @param distMap distance map on the graph
     * @param dualVal dual value list
     */
    void solve(Map<Record, Double> distMap, List<Double> dualVal);

}
