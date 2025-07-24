//go:build ignore
#include "cpp/common/Solution.h"
#include <sstream>
#include <stack>
#include <string>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> exclusiveTime(int n, const vector<string> &logs) {
    auto helper = [](const string &str) {
      stringstream ss;
      string temp;
      int id;
      string type;
      int time;
      ss << str;
      getline(ss, temp, ':');
      id = stoi(temp);
      getline(ss, type, ':');
      getline(ss, temp, ':');
      time = stoi(temp);
      return make_tuple(id, type, time);
    };

    vector<int> ans(n, 0);
    stack<int> st;
    int total = 0;
    for (const auto &log : logs) {
      const auto &[id, type, time] = helper(log);
      if (type == "start") {
        st.emplace(total - time);
      } else {
        int s = st.top();
        st.pop();
        int diff = time + 1 - total + s;
        ans[id] += diff;
        total += diff;
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
  int n = json::parse(inputArray.at(0));
  vector<string> logs = json::parse(inputArray.at(1));
  return solution.exclusiveTime(n, logs);
}
