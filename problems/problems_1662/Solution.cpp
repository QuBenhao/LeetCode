//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

template <typename ForwardIters1, typename ForwardIters2,
          typename Compare = std::equal_to<>  // 默认使用标准相等比较
          >
bool areEqual(ForwardIters1 begin1, ForwardIters1 end1, ForwardIters2 begin2,
              ForwardIters2 end2, Compare comp = Compare()) {
  auto it1 = begin1, it2 = begin2;
  auto inner_it1 = it1->begin(), inner_it2 = it2->begin();
  while (it1 != end1 && it2 != end2) {
    while (inner_it1 != it1->end() && inner_it2 != it2->end()) {
      if (!comp(*inner_it1, *inner_it2)) {
        return false;
      }
      ++inner_it1;
      ++inner_it2;
    }
    if (inner_it1 == (*it1).end()) {
      ++it1;
      if (it1 != end1) {
        inner_it1 = it1->begin();
      }
    }
    if (inner_it2 == (*it2).end()) {
      ++it2;
      if (it2 != end2) {
        inner_it2 = it2->begin();
      }
    }
  }
  return it1 == end1 && it2 == end2;
}

class Solution {
public:
  bool arrayStringsAreEqual(vector<string> &word1, vector<string> &word2) {
    return areEqual(word1.begin(), word1.end(), word2.begin(), word2.end());
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
  vector<string> word1 = json::parse(inputArray.at(0));
  vector<string> word2 = json::parse(inputArray.at(1));
  return solution.arrayStringsAreEqual(word1, word2);
}
