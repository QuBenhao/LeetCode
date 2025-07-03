//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
  int highBit(int64_t num) {
    num |= num >> 1;
    num |= num >> 2;
    num |= num >> 4;
    num |= num >> 8;
    num |= num >> 16;
    return 63 - __builtin_clzl((num + 1) >> 1);
  }

public:
  char kthCharacter(long long k, const vector<int> &operations) {
    int count = 0;
    while (k > 1) {
      int idx = highBit(k - 1);
      if (operations[idx] == 1) {
        ++count;
      }
      k -= 1LL << idx;
    }
    return 'a' + count % 26;
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
  long long k = json::parse(inputArray.at(0));
  vector<int> operations = json::parse(inputArray.at(1));
  return std::string(1, solution.kthCharacter(k, operations));
}
