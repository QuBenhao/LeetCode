//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class MyCircularQueue {
private:
  vector<int> arr;
  int k, sz, idx;

public:
  explicit MyCircularQueue(int k) : arr(k, -1), k(k), sz(0), idx(0) {}

  bool enQueue(int value) {
    if (sz == k) {
      return false;
    }
    arr[idx] = value;
    idx = (idx + 1) % k;
    ++sz;
    return true;
  }

  bool deQueue() {
    if (sz == 0) {
      return false;
    }
    --sz;
    return true;
  }

  int Front() {
    if (sz == 0) {
      return -1;
    }
    return arr[(idx - sz + k) % k];
  }

  int Rear() {
    if (sz == 0) {
      return -1;
    }
    return arr[(idx - 1 + k) % k];
  }

  bool isEmpty() { return sz == 0; }

  bool isFull() { return sz == k; }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
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
  auto obj0 = make_unique<MyCircularQueue>(op_values[0][0]);
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); ++i) {
    if (operators[i] == "enQueue") {
      ans.push_back(obj0->enQueue(op_values[i][0]));
      continue;
    }
    if (operators[i] == "deQueue") {
      ans.push_back(obj0->deQueue());
      continue;
    }
    if (operators[i] == "Front") {
      ans.push_back(obj0->Front());
      continue;
    }
    if (operators[i] == "Rear") {
      ans.push_back(obj0->Rear());
      continue;
    }
    if (operators[i] == "isEmpty") {
      ans.push_back(obj0->isEmpty());
      continue;
    }
    if (operators[i] == "isFull") {
      ans.push_back(obj0->isFull());
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
