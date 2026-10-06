//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minRefuelStops(int target, int startFuel, vector<vector<int>> &stations) {
    stations.push_back({target, 0});
    int ans = 0, pre_position = 0, cur_fuel = startFuel;
    priority_queue<int> fuel_heap;
    for (auto &station : stations) {
      int position = station[0];
      cur_fuel -= position - pre_position; // Each mile consumes 1 liter of fuel
      while (!fuel_heap.empty() && cur_fuel < 0) { // Out of fuel
        cur_fuel += fuel_heap.top();               // Choose the fuel can with the most fuel
        fuel_heap.pop();
        ans++;
      }
      if (cur_fuel < 0) { // Cannot reach the destination
        return -1;
      }
      fuel_heap.push(station[1]); // Save it for refueling later
      pre_position = position;
    }
    return ans;
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
  int target = json::parse(inputArray.at(0));
  int startFuel = json::parse(inputArray.at(1));
  vector<vector<int>> stations = json::parse(inputArray.at(2));
  return solution.minRefuelStops(target, startFuel, stations);
}
