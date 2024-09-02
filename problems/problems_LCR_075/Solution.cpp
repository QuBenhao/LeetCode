//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> relativeSortArray(vector<int> &arr1, vector<int> &arr2) {
    int mx = 0;
    for (int num : arr1) {
      mx = max(mx, num);
    }
    vector<int> freq(mx + 1);
    for (int num : arr1) {
      freq[num]++;
    }
    vector<int> ans;
    for (int num : arr2) {
      while (freq[num]-- > 0) {
        ans.push_back(num);
      }
    }
    for (int i = 0; i <= mx; i++) {
      while (freq[i]-- > 0) {
        ans.push_back(i);
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
  vector<int> arr1 = json::parse(inputArray.at(0));
  vector<int> arr2 = json::parse(inputArray.at(1));
  return solution.relativeSortArray(arr1, arr2);
}
