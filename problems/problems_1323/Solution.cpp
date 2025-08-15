//go:build ignore
#include "cpp/common/Solution.h"
#include <string>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maximum69Number(int num) {
    string s = to_string(num);
    for (char &c : s) {
      if (c == '6') {
        c = '9';
        break;
      }
    }
    return stoi(s);
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
}
