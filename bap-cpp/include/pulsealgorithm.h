#pragma once

class PulseAlgorithm {
private:
    void revise_cost_map();

public:
    PulseAlgorithm(/* args */);
    ~PulseAlgorithm();
    void solve();
};

