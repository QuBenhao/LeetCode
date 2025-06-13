//go:build ignore
#include "cpp/common/Solution.h"

#include <queue>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int furthestBuilding(vector<int> &heights, int bricks, int ladders) {
    priority_queue<int> maxHeap;
    int n = heights.size();
    for (int i = 0; i < n - 1; ++i) {
      int diff = heights[i + 1] - heights[i];
      if (diff <= 0)
        continue;
      if (bricks >= diff) {
        bricks -= diff;
        maxHeap.push(diff);
      } else {
        if (ladders > 0) {
          if (!maxHeap.empty() && maxHeap.top() > diff) {
            bricks += maxHeap.top() - diff;
            maxHeap.pop();
            maxHeap.push(diff);
          }
          --ladders;
        } else {
          return i;
        }
      }
    }
    return n - 1;
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
  vector<int> heights = json::parse(inputArray.at(0));
  int bricks = json::parse(inputArray.at(1));
  int ladders = json::parse(inputArray.at(2));
  return solution.furthestBuilding(heights, bricks, ladders);
}
