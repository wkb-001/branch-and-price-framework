#pragma once;
#include <problemcolumn.h>


class PricingProblem {
private:
    ProblemColumn shortest_path;
    double reduced_cost;

public:
    PricingProblem(/* args */);
    ~PricingProblem();
    void solve();
};
