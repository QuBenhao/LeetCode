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
  ListNode *reverseKGroup(ListNode *head, int k) {
    if (head == nullptr || k == 1) {
      return head;
    }
    ListNode *node = head;
    for (int i = 0; i < k - 1; i++) {
      if (node == nullptr) {
        return head;
      }
      node = node->next;
    }
    if (node == nullptr) {
      return head;
    }
    node->next = reverseKGroup(node->next, k);
    ListNode *tail = node->next, *last = tail;
    while (head != last) {
      ListNode *next = head->next;
      head->next = tail;
      tail = head;
      head = next;
    }
    return node;
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
	int k = json::parse(inputArray.at(1));
	ListNode *res_ptr = solution.reverseKGroup(head, k);
	json final_ans = ListNodeToIntArray(res_ptr);
	// delete head;
	delete res_ptr;
	return final_ans;
}
