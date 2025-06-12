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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
		ListNode *slow = head, *fast = head;
		for (int i = 0; i < n; i++) {
			fast = fast->next;
		}
		if (fast == nullptr) {
			ListNode *temp = head;
			head = head->next; // Remove the first node
			temp->next = nullptr; // Disconnect the removed node
			delete temp; // Free the memory of the removed node
			return head;
		}
		while (fast->next != nullptr) {
			slow = slow->next;
			fast = fast->next;
		}
		ListNode *temp = slow->next; // Node to be removed
		slow->next = slow->next->next;
		temp->next = nullptr; // Disconnect the removed node
		delete temp; // Free the memory of the removed node
		return head;
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
	int n = json::parse(inputArray.at(1));
	ListNode *res_ptr = solution.removeNthFromEnd(head, n);
	json final_ans = ListNodeToIntArray(res_ptr);
	delete res_ptr;
	return final_ans;
}