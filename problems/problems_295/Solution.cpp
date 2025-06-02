//go:build ignore
#include "cpp/common/Solution.h"
#include <functional>
#include <queue>
#include <vector>

using namespace std;
using json = nlohmann::json;

class MedianFinder {
    priority_queue<int> left; // 最大堆
    priority_queue<int, vector<int>, greater<>> right; // 最小堆
public:
    MedianFinder() {

    }

    void addNum(int num) {
        if (left.size() == right.size()) { // 两边一样多，先加入右边，再把右边最小值给左边
            right.push(num);
            left.push(right.top());
            right.pop();
        } else { // 左边更多，加入左边后，将左边最大给右边（保持两边数量一致）
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
