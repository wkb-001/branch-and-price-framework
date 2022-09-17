#pragma once

#include "solution.h"
#include "restrictedmasterproblem.h"
#include "pricingproblem.h"
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;

class BapNode {
private:
    void update_feasible_path(RestrictedMasterProblem &rmp);
    void resolve_graph();

public:
    bool is_integral;
    int iteration;
    double node_obj;
    Solution solution;
    bool is_LP_feasible;
    BapNode *parent;
    tuple<int, int> branch_arc;
    int node_id;
    unordered_map<tuple<int, int>, double> dist_map;
    vector<int> infeasible_path_indices;

    void column_generation(RestrictedMasterProblem &rmp, PricingProblem &sp);


};