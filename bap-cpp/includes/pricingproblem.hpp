#pragma once;
#include <problemcolumn.hpp>


class pricingproblem {
private:
    ProblemColumn shortest_path;
    double reduced_cost;

public:
    pricingproblem(/* args */);
    ~pricingproblem();
    void solve();
};
