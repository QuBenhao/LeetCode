//go:build ignore
#include "cpp/common/Solution.h"

#include <stack>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxChunksToSorted(const vector<int> &arr) {
    stack<int> s;
    for (const auto &num : arr) {
      if (!s.empty() && s.top() > num) {
        int maxNum = s.top();
        s.pop();
        while (!s.empty() && s.top() > num) {
          s.pop();
        }
        s.push(maxNum);
      } else {
        s.push(num);
      }
    }
    return s.size();
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
  vector<int> arr = json::parse(inputArray.at(0));
  return solution.maxChunksToSorted(arr);
}
