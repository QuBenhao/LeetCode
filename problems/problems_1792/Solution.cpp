//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>

using namespace std;
using json = nlohmann::json;

struct Tp {
  double improvement;
  int pass;
  int total;
  Tp(double imp, int p, int t) : improvement(imp), pass(p), total(t) {}
  bool operator<(const Tp &other) const {
    return improvement < other.improvement;
  }
};

class Solution {
public:
  double maxAverageRatio(const vector<vector<int>> &classes,
                         int extraStudents) {
    priority_queue<Tp> pq;
    for (const auto &c : classes) {
      int pass = c[0], total = c[1];
      double imp = static_cast<double>(pass + 1) / (total + 1) - static_cast<double>(pass) / total;
      pq.emplace(imp, pass, total);
    }
    while (extraStudents-- > 0) {
      auto [_, pass, total] = pq.top();
      pq.pop();
      pass++;
      total++;
      double imp = static_cast<double>(pass + 1) / (total + 1) - static_cast<double>(pass) / total;
      pq.emplace(imp, pass, total);
    }
    double result = 0.0;
    while (!pq.empty()) {
      auto [_, pass, total] = pq.top();
      pq.pop();
      result += static_cast<double>(pass) / total;
    }
    return result / classes.size();
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
  vector<vector<int>> classes = json::parse(inputArray.at(0));
  int extraStudents = json::parse(inputArray.at(1));
  return solution.maxAverageRatio(classes, extraStudents);
}
