//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>
#include <vector>

using namespace std;
using json = nlohmann::json;

class RandomizedSet {
  vector<int> values;
  unordered_map<int, int> idxMap;

public:
  /** Initialize your data structure here. */
  RandomizedSet() {}

  /** Inserts a value to the set. Returns true if the set did not already
   * contain the specified element. */
  bool insert(int val) {
    auto iter = idxMap.find(val);
    if (iter != idxMap.end()) {
      return false;
    }
    values.push_back(val);
    idxMap[val] = values.size() - 1;
    return true;
  }

  /** Removes a value from the set. Returns true if the set contained the
   * specified element. */
  bool remove(int val) {
    auto iter = idxMap.find(val);
    if (iter == idxMap.end()) {
      return false;
    }
    auto idx = iter->second;
    int n = values.size() - 1;
    values[idx] = values[n];
    idxMap[values[n]] = idx;
    values.pop_back();
    idxMap.erase(val);
    return true;
  }

  /** Get a random element from the set. */
  int getRandom() {
    auto idx = rand() % values.size();
    return values[idx];
  }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
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
  auto obj0 = make_shared<RandomizedSet>();
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); i++) {
    if (operators[i] == "insert") {
      ans.push_back(obj0->insert(op_values[i][0]));
      continue;
    }
    if (operators[i] == "remove") {
      ans.push_back(obj0->remove(op_values[i][0]));
      continue;
    }
    if (operators[i] == "getRandom") {
      ans.push_back(obj0->getRandom());
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
