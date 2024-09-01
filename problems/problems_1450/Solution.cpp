//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int busyStudent(vector<int> &startTime, vector<int> &endTime, int queryTime) {
    int ans = 0;
    for (size_t i = 0; i < startTime.size(); i++) {
      if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
        ans++;
      }
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
  vector<int> startTime = json::parse(inputArray.at(0));
  vector<int> endTime = json::parse(inputArray.at(1));
  int queryTime = json::parse(inputArray.at(2));
  return solution.busyStudent(startTime, endTime, queryTime);
}
