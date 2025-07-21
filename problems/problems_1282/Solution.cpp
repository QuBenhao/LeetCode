//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<int>> groupThePeople(const vector<int> &groupSizes) {
    unordered_map<int, vector<vector<int>>> groups;
    for (int i = 0; i < groupSizes.size(); ++i) {
      int size = groupSizes[i];
      if (!groups.contains(size) || groups[size].back().size() == size) {
        groups[size].emplace_back(vector<int>{i});
      } else {
        groups[size].back().push_back(i);
      }
    }
    vector<vector<int>> result;
    for (auto &pair : groups) {
      for (auto &group : pair.second) {
        result.emplace_back(std::move(group));
      }
    }
    return result;
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
  vector<int> groupSizes = json::parse(inputArray.at(0));
  return solution.groupThePeople(groupSizes);
}
