//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

const static int MAX_LEVEL = 16;
const static double P = 0.25;

struct SkipNode {
  int val;
  vector<SkipNode*> forward;
  SkipNode(int value, int level) : val(value), forward(level, nullptr) {}
};

class Skiplist {
  SkipNode* head;
  int level;

  int randomLevel() {
    int lvl = 0;
    while (rand() % 100 < P * 100 && lvl < MAX_LEVEL - 1) {
      lvl++;
    }
    return lvl;
  }

  SkipNode* searchWithUpdate(int target, vector<SkipNode*>& update) {
    SkipNode* current = head;
    for (int i = level; i >= 0; --i) {
      while (current->forward[i] != nullptr &&
             current->forward[i]->val < target) {
        current = current->forward[i];
      }
      update[i] = current;  // each update[i] will point to the last node before
                            // the target
    }
    return current->forward[0];
  }

 public:
  explicit Skiplist() : level(0) { head = new SkipNode(-1, MAX_LEVEL); }

  ~Skiplist() {
    SkipNode* current = head;
    while (current != nullptr) {
      SkipNode* next = current->forward[0];
      delete current;
      current = next;
    }
  }

  bool search(int target) {
    SkipNode* current = head;
    for (int i = level; i >= 0; --i) {
      while (current->forward[i] != nullptr &&
             current->forward[i]->val < target) {
        current = current->forward[i];
      }
    }
    current = current->forward[0];
    return current != nullptr && current->val == target;
  }

  void add(int num) {
    vector<SkipNode*> update(MAX_LEVEL, nullptr);
    searchWithUpdate(num, update);
    // if (current != nullptr && current->val == num) {
    // 	return; // Already exists
    // }

    int newLevel = randomLevel();
    if (newLevel > level) {
      for (int i = level + 1; i <= newLevel; ++i) {
        update[i] = head;
      }
      level = newLevel;
    }
    SkipNode* newNode = new SkipNode(num, newLevel + 1);
    for (int i = 0; i <= newLevel; ++i) {
      newNode->forward[i] =
          update[i]->forward[i];  // link new node's forward pointers with
                                  // current next nodes
      update[i]->forward[i] =
          newNode;  // link update nodes' forward pointers to new node
    }
  }

  bool erase(int num) {
    vector<SkipNode*> update(MAX_LEVEL, nullptr);
    SkipNode* current = searchWithUpdate(num, update);
    if (current != nullptr && current->val == num) {
      for (int i = 0; i <= level; ++i) {
        if (update[i]->forward[i] != current) {  // no need to continue as we
                                                 // have already erased the node
          break;
        }
        update[i]->forward[i] =
            current->forward[i];  // unlink the node from the skiplist
      }
      delete current;

      while (level > 0 &&
             head->forward[level] ==
                 nullptr) {  // If the highest level is empty, reduce the level
        level--;
      }
      return true;
    }
    return false;  // Not found
  }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
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
  auto obj0 = make_shared<Skiplist>();
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); i++) {
    if (operators[i] == "search") {
      ans.push_back(obj0->search(op_values[i][0]));
      continue;
    }
    if (operators[i] == "add") {
      obj0->add(op_values[i][0]);
      ans.push_back(nullptr);
      continue;
    }
    if (operators[i] == "erase") {
      ans.push_back(obj0->erase(op_values[i][0]));
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
