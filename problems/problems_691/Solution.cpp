//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>
#include <unordered_set>
#include <utility>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minStickers(const vector<string> &stickers, const string &target) {
    unordered_set<char> targetSet(target.begin(), target.end());
    vector<unordered_map<char, int>> available;
    auto trans = [&targetSet](const string &s) {
      unordered_map<char, int> count;
      for (char c : s) {
        if (targetSet.count(c)) {
          count[c]++;
        }
      }
      return count;
    };
    for (const auto &st : stickers) {
      const auto &count = trans(st);
      if (count.empty())
        continue;
      available.emplace_back(count);
    }
    queue<pair<string, int>> q;
    q.emplace(target, 0);
    unordered_set<string> visited{target};
    while (!q.empty()) {
      const auto &[cur, step] = q.front();
      if (cur.empty()) {
        return step;
      }
      for (const auto &count : available) {
        string next = cur;
        for (const auto &[c, v] : count) {
          for (int i = 0; i < v; i++) {
            auto pos = next.find(c);
            if (pos != string::npos) {
              next.erase(pos, 1);
            }
          }
        }
        if (visited.insert(next).second) {
          q.emplace(next, step + 1);
        }
      }
      q.pop();
    }
    return -1;
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
  vector<string> stickers = json::parse(inputArray.at(0));
  string target = json::parse(inputArray.at(1));
  return solution.minStickers(stickers, target);
}
