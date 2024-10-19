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
private:
  ListNode *reverse(ListNode *head) {
    ListNode *prev = nullptr;
    ListNode *curr = head;
    while (curr != nullptr) {
      ListNode *next = curr->next;
      curr->next = prev;
      prev = curr;
      curr = next;
    }
    return prev;
  }

public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    l1 = reverse(l1);
    l2 = reverse(l2);
    ListNode *dummy = new ListNode(0);
    ListNode *curr = dummy;
    int carry = 0;
    while (l1 != nullptr || l2 != nullptr) {
      int sum = carry;
      if (l1 != nullptr) {
        sum += l1->val;
        l1 = l1->next;
      }
      if (l2 != nullptr) {
        sum += l2->val;
        l2 = l2->next;
      }
      curr->next = new ListNode(sum % 10);
      carry = sum / 10;
      curr = curr->next;
    }
    if (carry > 0) {
      curr->next = new ListNode(carry);
    }
    return reverse(dummy->next);
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
  std::vector<int> l1_array = json::parse(inputArray.at(0));
  ListNode *l1 = IntArrayToListNode(l1_array);
  std::vector<int> l2_array = json::parse(inputArray.at(1));
  ListNode *l2 = IntArrayToListNode(l2_array);
  return ListNodeToIntArray(solution.addTwoNumbers(l1, l2));
}
