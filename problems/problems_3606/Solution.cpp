//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

const array<string, 4> business = {"electronics", "grocery", "pharmacy",
                                   "restaurant"};

class Solution {
public:
  vector<string> validateCoupons(const vector<string> &code,
                                 const vector<string> &businessLine,
                                 const vector<bool> &isActive) {
    int n = code.size();
    vector<int> valids;
    for (int i = 0; i < n; ++i) {
      if (!isActive[i]) {
        continue;
      }
      if (find(business.begin(), business.end(), businessLine[i]) ==
          business.end()) {
        continue;
      }
      if (code[i].empty()) {
        continue;
      }
      bool valid = true;
      for (char c : code[i]) {
        if (!isalnum(c) && c != '_') {
          valid = false;
          break;
        }
      }
      if (valid) {
        valids.push_back(i);
      }
    }
    sort(valids.begin(), valids.end(), [&businessLine, &code](int a, int b) {
      auto itA = find(business.begin(), business.end(), businessLine[a]);
      auto itB = find(business.begin(), business.end(), businessLine[b]);
      if (itA != itB) {
        return itA < itB;  // Sort by business line
      }
      return code[a] < code[b];  // Sort by code if business lines are the same
    });
    vector<string> result(valids.size());
    for (int i = 0; i < valids.size(); ++i) {
      result[i] = code[valids[i]];
    }
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
  vector<string> code = json::parse(inputArray.at(0));
  vector<string> businessLine = json::parse(inputArray.at(1));
  vector<bool> isActive = json::parse(inputArray.at(2));
  return solution.validateCoupons(code, businessLine, isActive);
}
