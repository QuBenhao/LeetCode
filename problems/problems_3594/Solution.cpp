//go:build ignore
#include <vector>
#include <queue>

#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

void combinations(vector<int> &result, const vector<int> &elements, int k) {
    int n = elements.size();
    vector<bool> v(n);
    fill(v.begin() + n - k, v.end(), true);
    do {
        int combination = 0;
        for (int i = 0; i < n; ++i) {
            if (v[i]) {
                combination |= 1 << elements[i];
            }
        }
        result.push_back(combination);
    } while (next_permutation(v.begin(), v.end()));
}

struct State {
    double time;
    int mask;
    int m;
    int side;

    bool operator<(const State &other) const {
        return time > other.time; // Min-heap based on time
    }
};

class Solution {
public:
    double minTime(int n, int k, int m, vector<int> &time, vector<double> &mul) {
        int total_mask = 1 << n;
        int init_mask = total_mask - 1;
        vector<vector<int>> graph(total_mask);
        for (int i = 1; i < total_mask; ++i) {
            vector<int> bits;
            int bit_count = 0;
            for (int j = 0; j < n; ++j) {
                if (i & (1 << j)) {
                    bits.push_back(j);
                    ++bit_count;
                }
            }
            for (int j = 1; j <= min(k, bit_count); ++j) {
                combinations(graph[i], bits, j);
            }
        }
        vector<vector<vector<double>>> dp(total_mask, vector<vector<double>>(m, vector<double>(2, 0x3f3f3f3f)));
        dp[init_mask][0][0] = 0.0;
        priority_queue<State> pq;
        pq.emplace(0.0, init_mask, 0, 0);

        while (!pq.empty()) {
            auto [current_time, current_mask, current_m, current_side] = pq.top();
            pq.pop();
            if (dp[current_mask][current_m][current_side] < current_time) {
                continue;
            }
            if (current_side == 0) {
                for (const auto &picks: graph[current_mask]) {
                    int max_time = 0;
                    int next_mask = current_mask & ~picks;
                    for (int j = 0; j < n; ++j) {
                        if (picks & (1 << j)) {
                            max_time = max(max_time, time[j]);
                        }
                    }
                    double use_time = mul[current_m] * max_time;
                    double next_time = current_time + use_time;
                    int next_m = (current_m + (int)floor(use_time)) % m;
                    if (dp[next_mask][next_m][1] > next_time) {
                        dp[next_mask][next_m][1] = next_time;
                        pq.emplace(next_time, next_mask, next_m, 1);
                    }
                }
            } else {
                if (current_mask == 0) {
                    return current_time;
                }
                for (int j = 0; j < n; ++j) {
                    if ((current_mask & (1 << j)) == 0) {
                        int next_mask = current_mask | (1 << j);
                        double use_time = mul[current_m] * time[j];
                        double next_time = current_time + use_time;
                        int next_m = (current_m + (int)floor(use_time)) % m;
                        if (dp[next_mask][next_m][0] > next_time) {
                            dp[next_mask][next_m][0] = next_time;
                            pq.emplace(next_time, next_mask, next_m, 0);
                        }
                    }
                }
            }
        }
        return -1.0;
    }
};

json leetcode::qubh::Solve(string input_json_values) {
    vector<string> inputArray;
    size_t pos = input_json_values.find('\n');
    while (pos != string::npos) {
        inputArray.push_back(input_json_values.substr(0, pos));
        input_json_values = input_json_values.substr(pos + 1);
        pos = input_json_values.find('\n');
    }
    inputArray.push_back(input_json_values);

    Solution solution;
    int n = json::parse(inputArray.at(0));
    int k = json::parse(inputArray.at(1));
    int m = json::parse(inputArray.at(2));
    vector<int> time = json::parse(inputArray.at(3));
    vector<double> mul = json::parse(inputArray.at(4));
    return solution.minTime(n, k, m, time, mul);
}
