//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
    size_t n = gas.size();
    int total_tank = 0;
    int curr_tank = 0;
    int starting_station = 0;
    for (size_t i = 0; i < n; ++i) {
      total_tank += gas[i] - cost[i];
      curr_tank += gas[i] - cost[i];
      if (curr_tank < 0) {
        starting_station = i + 1;
        curr_tank = 0;
      }
    }
    return total_tank >= 0 ? starting_station : -1;
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
  vector<int> gas = json::parse(inputArray.at(0));
  vector<int> cost = json::parse(inputArray.at(1));
  return solution.canCompleteCircuit(gas, cost);
}
