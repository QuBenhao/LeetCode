//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>

using namespace std;
using json = nlohmann::json;

class RecentCounter {
private:
  queue<int> q;

public:
  RecentCounter() {}

  int ping(int t) {
    while (!q.empty() && q.front() < t - 3000) {
      q.pop();
    }
    q.push(t);
    return static_cast<int>(q.size());
  }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
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
  auto obj0 = make_shared<RecentCounter>();
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); i++) {
    if (operators[i] == "ping") {
      ans.push_back(obj0->ping(op_values[i][0]));
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
