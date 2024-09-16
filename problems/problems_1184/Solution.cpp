//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int distanceBetweenBusStops(vector<int> &distance, int start,
                              int destination) {
    int n = static_cast<int>(distance.size()), mn = min(start, destination),
        mx = max(start, destination);
    int clock = 0, counterclock = 0;
    for (int i = mn; i < mx; i++) {
      clock += distance[i];
    }
    for (int i = mx; i < n + mn; i++) {
      counterclock += distance[i % n];
    }
    return min(clock, counterclock);
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
  vector<int> distance = json::parse(inputArray.at(0));
  int start = json::parse(inputArray.at(1));
  int destination = json::parse(inputArray.at(2));
  return solution.distanceBetweenBusStops(distance, start, destination);
}
