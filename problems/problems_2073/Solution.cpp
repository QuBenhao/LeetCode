//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int timeRequiredToBuy(vector<int> &tickets, int k) {
    int ans = 0, ticket_to_buy = tickets[k],
        n = static_cast<int>(tickets.size());
    for (int i = 0; i < n; i++) {
      ans += min(tickets[i], ticket_to_buy - (i > k ? 1 : 0));
    }
    return ans;
  };
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
  vector<int> tickets = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.timeRequiredToBuy(tickets, k);
}
