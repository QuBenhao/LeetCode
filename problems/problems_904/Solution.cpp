//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int totalFruit(vector<int> &fruits) {
    int ans = 0;
    int left = 0;
    int n = fruits.size();
    unordered_map<int, int> count(3);
    for (int right = 0; right < n; ++right) {
      count[fruits[right]]++;
      while (count.size() > 2) {
        count[fruits[left]]--;
        if (count[fruits[left]] == 0) {
          count.erase(fruits[left]);
        }
        left++;
      }
      ans = max(ans, right - left + 1);
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
  vector<int> fruits = json::parse(inputArray.at(0));
  return solution.totalFruit(fruits);
}
