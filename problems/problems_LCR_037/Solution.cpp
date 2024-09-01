//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> asteroidCollision(vector<int> &asteroids) {
    vector<int> stack;
    int n = static_cast<int>(asteroids.size());
    for (int i = 0; i < n; ++i) {
      while (!stack.empty() && stack.back() > 0 &&
             stack.back() < -asteroids[i]) {
        stack.pop_back();
      }
      if (stack.empty() || asteroids[i] > 0 || stack.back() < 0) {
        stack.push_back(asteroids[i]);
      } else if (stack.back() == -asteroids[i]) {
        stack.pop_back();
      }
    }
    return stack;
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
  vector<int> asteroids = json::parse(inputArray.at(0));
  return solution.asteroidCollision(asteroids);
}
