//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> asteroidCollision(const vector<int> &asteroids) {
    vector<int> stack(asteroids.size());
    int index = 0;
    for (const auto &asteroid : asteroids) {
      if (asteroid > 0) {
        stack[index++] = asteroid;
      } else {
        while (index > 0 && stack[index - 1] > 0 &&
               stack[index - 1] < -asteroid) {
          --index;
        }
        if (index == 0 || stack[index - 1] < 0) {
          stack[index++] = asteroid;
        } else if (stack[index - 1] == -asteroid) {
          --index;
        }
      }
    }
    stack.resize(index);
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
