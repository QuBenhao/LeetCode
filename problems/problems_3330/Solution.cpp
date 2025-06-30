//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int possibleStringCount(const string& word) {
    int ans = 1, n = word.size();
    for (int i = 0; i < n - 1; ++i) {
      if (word[i] == word[i + 1]) {
        ++ans;
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
  string word = json::parse(inputArray.at(0));
  return solution.possibleStringCount(word);
}
