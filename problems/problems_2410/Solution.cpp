//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int matchPlayersAndTrainers(vector<int> &players, vector<int> &trainers) {
    sort(players.begin(), players.end());
    sort(trainers.begin(), trainers.end());
    int ans = 0;
    int m = players.size(), n = trainers.size();
    for (int i = 0, j = 0; i < m && j < n; ++j) {
      if (players[i] <= trainers[j]) {
        ++ans;
        ++i;
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
  vector<int> players = json::parse(inputArray.at(0));
  vector<int> trainers = json::parse(inputArray.at(1));
  return solution.matchPlayersAndTrainers(players, trainers);
}
