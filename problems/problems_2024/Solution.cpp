//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxConsecutiveAnswers(string answerKey, int k) {
    int n = static_cast<int>(answerKey.size());
    int ans = 0;
    unordered_map<char, int> cnt;
    for (int l = 0, r = 0; r < n; ++r) {
      ++cnt[answerKey[r]];
      while (min(cnt['T'], cnt['F']) > k) {
        --cnt[answerKey[l++]];
      }
      ans = max(ans, r - l + 1);
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
  string answerKey = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.maxConsecutiveAnswers(answerKey, k);
}
