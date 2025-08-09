//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

bool inited = false;
array<unordered_map<int, int>, 31> powerOf2Digits;
void init() {
  if (inited)
    return;
  for (int i = 0; i < 31; i++) {
    int num = 1 << i;
    unordered_map<int, int> digitCount;
    while (num) {
      digitCount[num % 10]++;
      num /= 10;
    }
    powerOf2Digits[i] = digitCount;
  }
  inited = true;
}

class Solution {
public:
  bool reorderedPowerOf2(int n) {
    init();
    unordered_map<int, int> digitCount;
    while (n) {
      digitCount[n % 10]++;
      n /= 10;
    }
    for (const auto &powerDigits : powerOf2Digits) {
      if (powerDigits == digitCount)
        return true;
    }
    return false;
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
  return solution.reorderedPowerOf2(n);
}
