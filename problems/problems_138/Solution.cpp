//go:build ignore
#include "cpp/common/Solution.h"

#include "cpp/models/NodeRandom.h"

using namespace std;
using json = nlohmann::json;

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
  Node *copyRandomList(Node *head) {
    if (head == nullptr) {
      return nullptr;
    }
    Node *cur = head, *next;
    while (cur != nullptr) {
      next = cur->next;
      cur->next = new Node(cur->val);
      cur->next->next = next;
      cur = next;
    }
    cur = head;
    while (cur != nullptr) {
      cur->next->random = cur->random == nullptr ? nullptr : cur->random->next;
      cur = cur->next->next;
    }
    cur = head;
    Node *copy_head = head->next;
    while (cur != nullptr) {
      next = cur->next->next;
      cur->next->next = next == nullptr ? nullptr : next->next;
      cur->next = next;
      cur = next;
    }
    return copy_head;
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
  Node *head = JsonArrayToNodeRandom(json::parse(inputArray.at(0)));
  Node *copyHead = solution.copyRandomList(head);
  json res = NodeRandomToJsonArray(copyHead);
  delete head; // Clean up the original list to avoid memory leaks
  delete copyHead; // Clean up the copied list to avoid memory leaks
  return res;
}
