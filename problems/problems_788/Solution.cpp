//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

bool inited = false;
array<int, 10001> ans;
void init() {
  if (inited)
    return;
  inited = true;
  auto isNotRotatable = [](int c) { return c == 3 || c == 4 || c == 7; };
  auto isDiffRotatable = [](int c) {
    return c == 2 || c == 5 || c == 6 || c == 9;
  };
  for (int i = 1; i <= 10000; ++i) {
    bool notRotatable = false;
    bool diffRotatable = false;
    for (int j = i; j > 0; j /= 10) {
      int c = j % 10;
      if (isNotRotatable(c)) {
        notRotatable = true;
        break;
      }
      if (isDiffRotatable(c)) {
        diffRotatable = true;
      }
    }
    ans[i] = notRotatable ? ans[i - 1] : ans[i - 1] + (diffRotatable ? 1 : 0);
  }
}

class Solution {
public:
  int rotatedDigits(int n) {
    if (!inited) {
      init();
    }
    return ans[n];
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
  return solution.rotatedDigits(n);
}
