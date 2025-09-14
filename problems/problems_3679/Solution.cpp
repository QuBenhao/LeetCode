//go:build ignore
#include "cpp/common/Solution.h"
#include <deque>
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minArrivalsToDiscard(const vector<int> &arrivals, int w, int m) {
    deque<int> dq;
    unordered_map<int, int> counter;
    int ans = 0;
    int n = arrivals.size();
    for (int i = 0; i < n; ++i) {
      while (!dq.empty() && dq.front() < i - w + 1) {
        --counter[arrivals[dq.front()]];
        dq.pop_front();
      }
      if (counter[arrivals[i]] == m) {
        ++ans;
      } else {
        ++counter[arrivals[i]];
        dq.push_back(i);
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
  vector<int> arrivals = json::parse(inputArray.at(0));
  int w = json::parse(inputArray.at(1));
  int m = json::parse(inputArray.at(2));
  return solution.minArrivalsToDiscard(arrivals, w, m);
}
