//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/ListNode.h"

using namespace std;
using json = nlohmann::json;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
  ListNode *sortList(ListNode *head) {
    if (head == nullptr || head->next == nullptr) {
      return head;
    }
    ListNode *slow = head, *fast = head->next;
    while (fast != nullptr && fast->next != nullptr) {
      slow = slow->next;
      fast = fast->next->next;
    }
    ListNode *mid = slow->next;
    slow->next = nullptr;
    ListNode *left = sortList(head), *right = sortList(mid);
    ListNode *dummy = new ListNode(0), *node = dummy;
    while (left != nullptr && right != nullptr) {
      if (left->val < right->val) {
        node->next = left;
        left = left->next;
      } else {
        node->next = right;
        right = right->next;
      }
      node = node->next;
    }
    node->next = left != nullptr ? left : right;
    return dummy->next;
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
  std::vector<int> head_array = json::parse(inputArray.at(0));
  ListNode *head = IntArrayToListNode(head_array);
  return ListNodeToIntArray(solution.sortList(head));
}
