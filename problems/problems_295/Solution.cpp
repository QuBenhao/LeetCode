//go:build ignore
#include "cpp/common/Solution.h"
#include <functional>
#include <queue>
#include <vector>

using namespace std;
using json = nlohmann::json;

class MedianFinder {
private:
  priority_queue<int> max_heap;
  priority_queue<int, vector<int>, greater<int>> min_heap;

public:
  MedianFinder() {
    max_heap = priority_queue<int>();
    min_heap = priority_queue<int, vector<int>, greater<int>>();
  }

  void addNum(int num) {
    if (min_heap.size() == max_heap.size()) {
      if (min_heap.empty() || num <= min_heap.top()) {
        max_heap.push(num);
      } else {
        max_heap.push(min_heap.top());
        min_heap.pop();
        min_heap.push(num);
      }
    } else {
      if (num >= max_heap.top()) {
        min_heap.push(num);
      } else {
        min_heap.push(max_heap.top());
        max_heap.pop();
        max_heap.push(num);
      }
    }
  }

  double findMedian() {
    return min_heap.size() == max_heap.size()
               ? static_cast<double>(min_heap.top() + max_heap.top()) / 2.0
               : max_heap.top();
  }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
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
  auto obj0 = make_shared<MedianFinder>();
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); i++) {
    if (operators[i] == "addNum") {
      obj0->addNum(op_values[i][0]);
      ans.push_back(nullptr);
      continue;
    }
    if (operators[i] == "findMedian") {
      ans.push_back(obj0->findMedian());
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
