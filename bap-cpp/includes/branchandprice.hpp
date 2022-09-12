#pragma once

#include "restrictedmasterproblem.hpp"
#include "pricingproblem.hpp"
#include "bapnode.hpp"
#include <queue>
using namespace std;

class BranchAndPrice {
private:
    BapNode best_node;

    void branch_and_bound();
    void add_node_queue();

public:
    bool silent;
    bool opt_flag;
    RestrictedMasterProblem *rmp;
    PricingProblem *sp;
    // solution information
    int node_explored;
    int total_cg_iteration;
    double mip_search_gap;
    double cpu_time;
    double lb;
    double ub;
    double root_relaxation_val;
    priority_queue<BapNode, vector<BapNode>, greater<BapNode>> queue;
    priority_queue<Solution, vector<Solution>, greater<Solution>> solution_pool;

    void print_solution();
    bool solve();

};
