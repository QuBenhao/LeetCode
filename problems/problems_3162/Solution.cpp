//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int numberOfPairs(vector<int> &nums1, vector<int> &nums2, int k) {
    unordered_map<int, int> counter;
    for (int num : nums1) {
      if (num % k != 0) {
        continue;
      }
      num /= k;
      for (int i = 1; i * i <= num; i++) {
        if (num % i != 0) {
          continue;
        }
        counter[i]++;
        if (i * i != num) {
          counter[num / i]++;
        }
      }
    }
    int ans = 0;
    for (int num : nums2) {
      ans += counter[num];
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
  vector<int> nums1 = json::parse(inputArray.at(0));
  vector<int> nums2 = json::parse(inputArray.at(1));
  int k = json::parse(inputArray.at(2));
  return solution.numberOfPairs(nums1, nums2, k);
}
