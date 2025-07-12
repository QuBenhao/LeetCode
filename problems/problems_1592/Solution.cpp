//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string reorderSpaces(const string &text) {
    int space = 0, n = text.length();
    vector<string> words;
    for (int i = 0, start = -1; i <= n; ++i) {
      if (i == n || text[i] == ' ') {
        if (start != -1) {
          words.emplace_back(text.substr(start, i - start));
        }
        start = -1;
        ++space;
      } else if (start == -1) {
        start = i;
      }
    }
    --space;
    int m = words.size();
    if (m == 1) {
      return words[0] + string(space, ' ');
    }
    int gap = space / (m - 1), remain = space % (m - 1);
    string result;
    for (int i = 0; i < m; ++i) {
      result += words[i];
      if (i < m - 1) {
        result += string(gap, ' ');
      }
    }
    return result + string(remain, ' ');
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
  string text = json::parse(inputArray.at(0));
  return solution.reorderSpaces(text);
}
