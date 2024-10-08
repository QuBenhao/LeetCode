//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_set>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string destCity(vector<vector<string>> &paths) {
    unordered_set<string> cities;
    for (auto &path : paths) {
      cities.insert(path.at(0));
    }
    for (auto &path : paths) {
      if (cities.find(path.at(1)) == cities.end()) {
        return path.at(1);
      }
    }
    return "";
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
  vector<vector<string>> paths = json::parse(inputArray.at(0));
  return solution.destCity(paths);
}
