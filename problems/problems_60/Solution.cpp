//go:build ignore
#include "cpp/common/Solution.h"
#include <numeric>

using namespace std;
using json = nlohmann::json;

array<int, 10> VALS;
bool inited = false;

class Solution {
public:
  string getPermutation(int n, int k) {
    if (!inited) {
      VALS[0] = 1;
      for (int i = 1; i < 10; ++i) {
        VALS[i] = VALS[i - 1] * i;
      }
      inited = true;
    }
    --k;
    string ans = "";
    vector<char> picks(n);
    iota(picks.begin(), picks.end(), '1');
    for (; n > 0; --n) {
      int d = k / VALS[n - 1];
      ans += picks[d];
      picks.erase(picks.begin() + d);
      k %= VALS[n - 1];
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
  int n = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.getPermutation(n, k);
}
