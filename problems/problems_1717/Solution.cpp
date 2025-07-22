//go:build ignore
#include "cpp/common/Solution.h"
#include <functional>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maximumGain(const string &s, int x, int y) {
    int n = s.length();
    function<bool(int)> isA, isB;

    if (x < y) {
      swap(x, y);
      isA = [&s](int idx) { return s[idx] == 'b'; };
      isB = [&s](int idx) { return s[idx] == 'a'; };
    } else {
      isA = [&s](int idx) { return s[idx] == 'a'; };
      isB = [&s](int idx) { return s[idx] == 'b'; };
    }
    int ans = 0;
    int i = 0;
    while (i < n) {
      while (i < n && !isA(i) && !isB(i)) {
        ++i;
      }

      int ca = 0, cb = 0;
      while (i < n && (isA(i) || isB(i))) {
        if (isA(i)) {
          ++ca;
        } else {
          if (ca > 0) {
            ans += x;
            --ca;
          } else {
            ++cb;
          }
        }
        ++i;
      }
      ans += min(ca, cb) * y;
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
  string s = json::parse(inputArray.at(0));
  int x = json::parse(inputArray.at(1));
  int y = json::parse(inputArray.at(2));
  return solution.maximumGain(s, x, y);
}
