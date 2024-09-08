//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class DLinkedNode {
public:
  int key, value;
  DLinkedNode *prev;
  DLinkedNode *next;
  DLinkedNode() : key(0), value(0), prev(nullptr), next(nullptr) {}
  DLinkedNode(int _key, int _value)
      : key(_key), value(_value), prev(nullptr), next(nullptr) {}
};

class LRUCache {
private:
  unordered_map<int, DLinkedNode *> cache;
  DLinkedNode *head;
  DLinkedNode *tail;
  int capacity;

  void removeNode(DLinkedNode *node) {
    if (node->prev != nullptr) {
      node->prev->next = node->next;
    }
    if (node->next != nullptr) {
      node->next->prev = node->prev;
    }
  }

  void addToHead(DLinkedNode *node) {
    node->prev = head;
    node->next = head->next;
    head->next->prev = node;
    head->next = node;
  }

  void moveToHead(DLinkedNode *node) {
    removeNode(node);
    addToHead(node);
  }

  DLinkedNode *removeTail() {
    DLinkedNode *node = tail->prev;
    removeNode(node);
    return node;
  }

public:
  LRUCache(int capacity) {
    this->capacity = capacity;
    head = new DLinkedNode();
    tail = new DLinkedNode();
    head->next = tail;
    tail->prev = head;
  }

  int get(int key) {
    if (!cache.count(key)) {
      return -1;
    }
    DLinkedNode *node = cache[key];
    moveToHead(node);
    return node->value;
  }

  void put(int key, int value) {
    if (!cache.count(key)) {
      DLinkedNode *node = new DLinkedNode(key, value);
      cache[key] = node;
      addToHead(node);
      if (cache.size() > capacity) {
        DLinkedNode *removed = removeTail();
        cache.erase(removed->key);
        delete removed;
      }
    } else {
      DLinkedNode *node = cache[key];
      node->value = value;
      moveToHead(node);
    }
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
