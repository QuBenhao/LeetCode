// go:build ignore
#include "cpp/common/Solution.h"
#include <queue>

using namespace std;
using json = nlohmann::json;

class SeatManager {
private:
  priority_queue<int, vector<int>, greater<int>> q;

public:
  SeatManager(int n) {
    for (int i = 1; i <= n; i++) {
      q.push(i);
    }
  }

  int reserve() {
    int v = q.top();
    q.pop();
    return v;
  }

  void unreserve(int seatNumber) { q.push(seatNumber); }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
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
  auto obj0 = make_shared<SeatManager>(op_values[0][0]);
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); i++) {
    if (operators[i] == "reserve") {
      ans.push_back(obj0->reserve());
      continue;
    }
    if (operators[i] == "unreserve") {
      obj0->unreserve(op_values[i][0]);
      ans.push_back(nullptr);
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
