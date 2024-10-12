//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimumLengthEncoding(vector<string> &words) {
    int n = static_cast<int>(words.size());
    vector<string> revertWords = vector<string>(n);
    for (int i = 0; i < n; i++) {
      revertWords[i] = words[i];
      reverse(revertWords[i].begin(), revertWords[i].end());
    }
    sort(revertWords.begin(), revertWords.end());
    int ans = 0;
    for (int i = 0; i < n; i++) {
      if (i + 1 < n && revertWords[i + 1].find(revertWords[i]) == 0) {
        continue;
      }
      ans += revertWords[i].size() + 1;
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
  vector<string> words = json::parse(inputArray.at(0));
  return solution.minimumLengthEncoding(words);
}
