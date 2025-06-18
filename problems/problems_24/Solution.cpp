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
    ListNode* swapPairs(ListNode* head) {
		ListNode dummy = ListNode(0, head);
		ListNode* pre = &dummy, *cur = head;
		while (cur != nullptr && cur->next != nullptr) {
			ListNode* next = cur->next;
			pre->next = next;
			cur->next = next->next;
			next->next = cur;
			pre = cur;
			cur = cur->next;
		}
		cur = dummy.next;
		dummy.next = nullptr; // Disconnect the dummy node
		return cur; // Return the new head of the list
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
	ListNode *res_ptr = solution.swapPairs(head);
	json final_ans = ListNodeToIntArray(res_ptr);
	// delete head;
	delete res_ptr;
	return final_ans;
}
