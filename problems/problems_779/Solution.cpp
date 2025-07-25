//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int kthGrammar(int n, int k) {
    if (n == 1) {
      return 0;
    }
    int parent = kthGrammar(n - 1, (k + 1) >> 1);
    return (1 - parent) ^ (k & 1);
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
  int n = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.kthGrammar(n, k);
}
