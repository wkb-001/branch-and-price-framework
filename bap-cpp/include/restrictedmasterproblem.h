#pragma once
#include "gurobi_c++.h"
#include "problemcolumn.h"
#include "solution.h"
#include <vector>
using namespace std;


class RestrictedMasterProblem {

public:
    GRBModel model;
    double obj_val;
    bool is_integral;
    vector<ProblemColumn> column_list;
    vector<double> dual_val;

    void init_model(vector<ProblemColumn> init_cols);
    void add_column(vector<ProblemColumn> column_list);
    bool optimize();
    Solution get_solution();

private:
    void set_lp_solver_param();

};