//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

constexpr int MAX_P = 50;
long long COMBNATIONS[MAX_P + 1][MAX_P + 1];
static bool init = []() {
  for (int i = 0; i <= MAX_P; ++i) {
    COMBNATIONS[i][0] = 1;
    for (int j = 1; j <= i; ++j)
      COMBNATIONS[i][j] = COMBNATIONS[i - 1][j] + COMBNATIONS[i - 1][j - 1];
  }
  return true;
}();

class Solution {
public:
  long long nthSmallest(long long n, int k) {
    long long ans = 0LL;
    for (int i = 49; i >= 0; --i) {
      if (COMBNATIONS[i][k] < n) {
        ans |= 1LL << i;
        n -= COMBNATIONS[i][k];
        --k;
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
  long long n = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.nthSmallest(n, k);
}
