package algorithm.pricingalgorithm;

import utils.PricingAlgorithm;

import java.util.List;
import java.util.Map;

public abstract class PulseAlgorithm implements PricingAlgorithm {
    
    @Override
    public abstract void reviseCostMap(Map<Record, Double> distMap, List<Double> dualVal);

    @Override
    public abstract void solve(Map<Record, Double> distMap, List<Double> dualVal);

}
