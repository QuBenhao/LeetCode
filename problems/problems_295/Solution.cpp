//go:build ignore
#include "cpp/common/Solution.h"
#include <functional>
#include <queue>
#include <vector>

using namespace std;
using json = nlohmann::json;

class MedianFinder {
    priority_queue<int> left; // Max-heap
    priority_queue<int, vector<int>, greater<>> right; // Min-heap
public:
    MedianFinder() {

    }

    void addNum(int num) {
        if (left.size() == right.size()) { // When both sides have the same size, insert into the right heap, then move its minimum to the left
            right.push(num);
            left.push(right.top());
            right.pop();
        } else { // When the left has more elements, insert there, then move its maximum to the right to balance the sizes
            left.push(num);
            right.push(left.top());
            left.pop();
        }
    }

    double findMedian() {
        if (left.size() == right.size()) {
            return (left.top() + right.top()) / 2.0;
        }
        return left.top();
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
