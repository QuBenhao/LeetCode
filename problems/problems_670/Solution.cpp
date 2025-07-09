//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maximumSwap(int num) {
    vector<int> digits;
    vector<int> maxDigits(10, -1);
    int n = 0;
    for (int x = num; x > 0; x /= 10) {
      int cur = x % 10;
      digits.push_back(cur);
      if (maxDigits[cur] == -1) {
        maxDigits[cur] = n;
      }
      ++n;
    }
    for (int i = n - 1; i > 0; --i) {
      for (int j = 9; j > digits[i]; --j) {
        if (maxDigits[j] != -1 && maxDigits[j] < i) {
          swap(digits[i], digits[maxDigits[j]]);
          int result = 0;
          for (int k = n - 1; k >= 0; --k) {
            result = result * 10 + digits[k];
          }
          return result;
        }
      }
    }
    return num;
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
  int num = json::parse(inputArray.at(0));
  return solution.maximumSwap(num);
}
