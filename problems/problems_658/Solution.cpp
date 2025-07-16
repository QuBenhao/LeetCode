//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> findClosestElements(const vector<int> &arr, int k, int x) {
    int n = arr.size();
    int right = upper_bound(arr.begin(), arr.end(), x) - arr.begin();
    int left = right - 1;
    x <<= 1;
    for (; k > 0 && left >= 0 && right < n; --k) {
      if (arr[left] + arr[right] >= x) {
        --left;
      } else {
        ++right;
      }
    }
    if (k > 0) {
      if (left < 0) {
        right += k;
      } else {
        left -= k;
      }
    }
    return vector<int>(arr.begin() + left + 1, arr.begin() + right);
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
  int k = json::parse(inputArray.at(1));
  int x = json::parse(inputArray.at(2));
  return solution.findClosestElements(arr, k, x);
}
