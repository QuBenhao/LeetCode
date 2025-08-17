//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

const double TARGET = 24.0;
const double EPSILON = 1e-6;

class Solution {
public:
  bool judgePoint24(const vector<int> &cards) {
    auto backtrack = [](this auto &&backtrack, const vector<double> &nums) -> bool {
      if (nums.size() == 1) {
        return abs(nums[0] - TARGET) < EPSILON;
      }
      for (int i = 0; i + 1 < nums.size(); ++i) {
        for (int j = i + 1; j < nums.size(); ++j) {
          vector<double> nextNums;
          for (int k = 0; k < nums.size(); ++k) {
            if (k != i && k != j) {
              nextNums.push_back(nums[k]);
            }
          }

          for (int op = 0; op < 6; ++op) {
            double a = nums[i], b = nums[j];
            switch (op) {
            case 0:
              nextNums.push_back(a + b);
              break;
            case 1:
              nextNums.push_back(a - b);
              break;
            case 2:
              nextNums.push_back(b - a);
              break;
            case 3:
              nextNums.push_back(a * b);
              break;
            case 4:
              if (abs(b) < EPSILON)
                continue;
              nextNums.push_back(a / b);
              break;
            case 5:
              if (abs(a) < EPSILON)
                continue;
              nextNums.push_back(b / a);
              break;
            }
            if (backtrack(nextNums))
              return true;
            nextNums.pop_back();
          }
        }
      }
      return false;
    };

    return backtrack({static_cast<double>(cards[0]), static_cast<double>(cards[1]), static_cast<double>(cards[2]), static_cast<double>(cards[3])});
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
  vector<int> cards = json::parse(inputArray.at(0));
  return solution.judgePoint24(cards);
}
