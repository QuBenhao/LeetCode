//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxTotalFruits(const vector<vector<int>> &fruits, int startPos, int k) {
    int left = lower_bound(fruits.begin(), fruits.end(), startPos - k,
                           [](const vector<int> &fruit, int pos) {
                             return fruit[0] < pos;
                           }) -
               fruits.begin();
    int ans = 0, s = 0;
    int n = fruits.size();
    int max_distance = startPos + k;
    for (int right = left; right < n && fruits[right][0] <= max_distance;
         ++right) {
      s += fruits[right][1];
      while (fruits[right][0] * 2 - fruits[left][0] - startPos > k &&
              fruits[right][0] + startPos - fruits[left][0] * 2 > k) {
        s -= fruits[left++][1];
      }
      ans = max(ans, s);
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
  vector<vector<int>> fruits = json::parse(inputArray.at(0));
  int startPos = json::parse(inputArray.at(1));
  int k = json::parse(inputArray.at(2));
  return solution.maxTotalFruits(fruits, startPos, k);
}
