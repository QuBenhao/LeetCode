//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maximumEnergy(vector<int> &energy, int k) {
    int n = energy.size();
    for (int i = n - k - 1; i >= 0; --i) {
      energy[i] += energy[i + k];
    }
    return *max_element(energy.begin(), energy.end());
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
  vector<int> energy = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.maximumEnergy(energy, k);
}
