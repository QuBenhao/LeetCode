//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimumDeletions(string word, int k) {
    array<int, 26> freq = {0};
    for (char c : word) {
      freq[c - 'a']++;
    }
    sort(freq.begin(), freq.end());
    int ans = word.length();
    for (int i = 0; i < 26; ++i) {
      int cur = 0, maxFreq = freq[i] + k;
      for (int j = 0; j < i; ++j) {
        if (freq[j] >= freq[i]) {
          break;
        }
        cur += freq[j];
      }
      for (int j = 25; j > i; --j) {
        if (freq[j] <= maxFreq) {
          break;
        }
        cur += freq[j];
      }
      ans = min(ans, cur);
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
  string word = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.minimumDeletions(word, k);
}
