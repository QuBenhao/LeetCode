//go:build ignore
#include "cpp/common/Solution.h"
#include <sstream>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string addBinary(string a, string b) {
    stringstream ss;
    int carry = 0;
    if (a.size() < b.size()) {
      swap(a, b);
    }
    int i = static_cast<int>(a.size()) - 1;
    int diff = static_cast<int>(a.size()) - static_cast<int>(b.size());
    while (i >= 0) {
      int sum = a[i] - '0' + (i - diff >= 0 ? b[i - diff] - '0' : 0) + carry;
      ss << sum % 2;
      carry = sum / 2;
      i--;
    }
    if (carry) {
      ss << carry;
    }
    string result = ss.str();
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
  string a = json::parse(inputArray.at(0));
  string b = json::parse(inputArray.at(1));
  return solution.addBinary(a, b);
}
