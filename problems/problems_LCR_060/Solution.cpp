//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> topKFrequent(vector<int> &nums, int k) {
    unordered_map<int, int> freq;
    for (int num : nums) {
      freq[num]++;
    }
    priority_queue<pair<int, int>, vector<pair<int, int>>,
                   greater<pair<int, int>>>
        pq;
    for (auto &[num, count] : freq) {
      pq.push({count, num});
      if (pq.size() > k) {
        pq.pop();
      }
    }
    vector<int> ans;
    while (!pq.empty()) {
      ans.push_back(pq.top().second);
      pq.pop();
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
  vector<int> nums = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.topKFrequent(nums, k);
}
