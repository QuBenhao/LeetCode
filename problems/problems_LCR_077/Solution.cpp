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
    ListNode *fast = head, *slow = head, *prev;
    while (fast != nullptr && fast->next != nullptr) {
      fast = fast->next->next;
      prev = slow;
      slow = slow->next;
    }
    prev->next = nullptr;
    ListNode *left = sortList(head);
    ListNode *right = sortList(slow);
    return mergeSort(left, right);
  }

private:
  ListNode *mergeSort(ListNode *l1, ListNode *l2) {
    if (l1 == nullptr) {
      return l2;
    }
    if (l2 == nullptr) {
      return l1;
    }
    ListNode *dummy = new ListNode();
    ListNode *cur = dummy;
    while (l1 != nullptr || l2 != nullptr) {
      if (l1 == nullptr || (l2 != nullptr && l2->val < l1->val)) {
        cur->next = l2;
        l2 = l2->next;
      } else {
        cur->next = l1;
        l1 = l1->next;
      }
      cur = cur->next;
    }
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
