//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

const string HEX_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

class Solution {
public:
  string concatHex36(int n) {
    string result;
    int x = n * n;
    int y = x * n;
    while (y > 0) {
      result += HEX_CHARS[y % 36];
      y /= 36;
    }
    while (x > 0) {
      result += HEX_CHARS[x % 16];
      x /= 16;
    }
    reverse(result.begin(), result.end());
    return result;
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
  return solution.concatHex36(n);
}
