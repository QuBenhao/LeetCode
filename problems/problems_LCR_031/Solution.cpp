//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class DoublyListNode {
public:
  int key, value;
  DoublyListNode *prev, *next;
  DoublyListNode(int _key, int _value)
      : key(_key), value(_value), prev(nullptr), next(nullptr) {}
  void insert(DoublyListNode *node) {
    node->prev = this;
    node->next = next;
    if (next != nullptr) {
      next->prev = node;
    }
    next = node;
  }
  void remove() {
    if (prev != nullptr) {
      prev->next = next;
    }
    if (next != nullptr) {
      next->prev = prev;
    }
  }
};

class LRUCache {
private:
  int capacity;
  unordered_map<int, DoublyListNode *> cache;
  DoublyListNode *head, *tail;

public:
  LRUCache(int capacity) {
    this->capacity = capacity;
    head = new DoublyListNode(-1, -1);
    tail = new DoublyListNode(-1, -1);
    head->next = tail;
    tail->prev = head;
  }

  int get(int key) {
    if (cache.find(key) == cache.end()) {
      return -1;
    }
    DoublyListNode *node = cache[key];
    node->remove();
    head->insert(node);
    return node->value;
  }

  void put(int key, int value) {
    DoublyListNode *node;
    if (cache.find(key) != cache.end()) {
      node = cache[key];
      node->remove();
      node->value = value;
    } else {
      if (cache.size() == capacity) {
        DoublyListNode *removed = tail->prev;
        removed->remove();
        cache.erase(removed->key);
      }
      node = new DoublyListNode(key, value);
      cache[key] = node;
    }
    head->insert(node);
  }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
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
  auto obj0 = make_shared<LRUCache>(op_values[0][0]);
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); i++) {
    if (operators[i] == "get") {
      ans.push_back(obj0->get(op_values[i][0]));
      continue;
    }
    if (operators[i] == "put") {
      obj0->put(op_values[i][0], op_values[i][1]);
      ans.push_back(nullptr);
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
