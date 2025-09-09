//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>
#include <unordered_set>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimumTeachings(int n, const vector<vector<int>> &languages,
                       const vector<vector<int>> &friendships) {
    vector<unordered_set<int>> languages_set;
    for (const auto &language : languages) {
      languages_set.emplace_back(language.begin(), language.end());
    }

    auto intersection = [](const unordered_set<int> &a,
                           const unordered_set<int> &b) -> bool {
      const unordered_set<int> *s1 = &a, *s2 = &b;
      if (a.size() > b.size()) {
        std::swap(s1, s2);
      }
      for (const auto &v : *s1) {
        if (s2->contains(v)) {
          return true;
        }
      }
      return false;
    };

    unordered_set<int> needs;
    for (const auto &friends : friendships) {
      int u = friends[0] - 1, v = friends[1] - 1;
      if (intersection(languages_set[u], languages_set[v])) {
        continue;
      }
      needs.insert(u);
      needs.insert(v);
    }

    if (needs.empty()) {
      return 0;
    }

    vector<int> count(n, 0);
    for (const auto &p : needs) {
      for (const auto &l : languages[p]) {
        ++count[l - 1];
      }
    }
    return needs.size() - ranges::max(count);
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
  vector<vector<int>> languages = json::parse(inputArray.at(1));
  vector<vector<int>> friendships = json::parse(inputArray.at(2));
  return solution.minimumTeachings(n, languages, friendships);
}
