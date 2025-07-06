//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool canFormArray(const vector<int> &arr, const vector<vector<int>> &pieces) {
    unordered_map<int, vector<int>> pieceMap;
    for (const auto &piece : pieces) {
      pieceMap[piece[0]] = piece;
    }

    for (int i = 0; i < arr.size();) {
      if (pieceMap.count(arr[i]) == 0)
        return false;
      const auto &piece = pieceMap[arr[i]];
      for (int j = 0; j < piece.size(); ++j) {
        if (i + j >= arr.size() || arr[i + j] != piece[j])
          return false;
      }
      i += piece.size();
    }
    return true;
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
  vector<int> arr = json::parse(inputArray.at(0));
  vector<vector<int>> pieces = json::parse(inputArray.at(1));
  return solution.canFormArray(arr, pieces);
}
