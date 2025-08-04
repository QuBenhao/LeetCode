//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

constexpr array<string, 4> DIRS = {"East", "North", "West", "South"};

class Robot {
private:
  int m, n, loc, total;
  bool moved;

  tuple<int, int, int> move() {
    if (!moved) {
      return {0, 0, 0};
    }
    if (loc < m) {
      return {loc, 0, loc == 0 ? 3 : 0};
    }
    if (loc < m + n - 1) {
      return {m - 1, loc - m + 1, 1};
    }
    if (loc < 2 * m + n - 2) {
      return {m - 1 - (loc - m - n + 2), n - 1, 2};
    }
    return {0, total - loc, 3};
  }

public:
  explicit Robot(int width, int height)
      : m(width), n(height), loc(0), moved(false) {
    total = 2 * (m + n) - 4;
  }

  void step(int num) {
    num %= total;
    loc = (loc + num) % total;
    moved = true;
  }

  vector<int> getPos() {
    const auto [x, y, _] = move();
    return {x, y};
  }

  string getDir() {
    const auto [_, __, dir] = move();
    return DIRS[dir];
  }
};

/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */

json leetcode::qubh::Solve(string input_json_values) {
  vector<string> inputArray;
  size_t pos = input_json_values.find('\n');
  while (pos != string::npos) {
    inputArray.push_back(input_json_values.substr(0, pos));
    input_json_values = input_json_values.substr(pos + 1);
    pos = input_json_values.find('\n');
  }
  inputArray.push_back(input_json_values);

  vector<string> operators = json::parse(inputArray[0]);
  vector<vector<json>> op_values = json::parse(inputArray[1]);
  auto obj0 = make_unique<Robot>(op_values[0][0], op_values[0][1]);
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); ++i) {
    if (operators[i] == "step") {
      obj0->step(op_values[i][0]);
      ans.push_back(nullptr);
      continue;
    }
    if (operators[i] == "getPos") {
      ans.push_back(obj0->getPos());
      continue;
    }
    if (operators[i] == "getDir") {
      ans.push_back(obj0->getDir());
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
