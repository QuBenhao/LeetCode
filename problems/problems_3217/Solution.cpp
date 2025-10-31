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
  ListNode *modifiedList(const vector<int> &nums, ListNode *head) {
    unordered_set<int> s(nums.begin(), nums.end());
    ListNode dummy(-1, head);
    ListNode *prev = &dummy, *curr = head;
    while (curr != nullptr) {
      ListNode *next = curr->next;
      if (s.contains(curr->val)) {
        prev->next = next;
        curr->next = nullptr;
        delete curr;
      } else {
        prev = curr;
      }
      curr = next;
    }
    ListNode *res = dummy.next;
    dummy.next = nullptr;
    return res;
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
  vector<int> nums = json::parse(inputArray.at(0));
  std::vector<int> head_array = json::parse(inputArray.at(1));
  ListNode *head = IntArrayToListNode(head_array);
  ListNode *res_ptr = solution.modifiedList(nums, head);
  json final_ans = ListNodeToIntArray(res_ptr);
  // delete head;
  delete res_ptr;
  return final_ans;
}
