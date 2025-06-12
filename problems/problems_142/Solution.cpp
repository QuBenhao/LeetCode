//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/ListNode.h"

#include <unordered_set>

using namespace std;
using json = nlohmann::json;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (head == nullptr) {
            return nullptr;
        }
        auto slow = head, fast = head;
        while (true) {
            if (fast == nullptr || fast->next == nullptr) {
                return nullptr;
            }
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                break;
            }
        }
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        return slow;
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
	int position = json::parse(inputArray.at(1));
	ListNode* head = IntArrayToListNodeCycle(head_array, position);
	ListNode *res_ptr = solution.detectCycle(head);
	if (res_ptr == nullptr) {
        delete head; // Delete the head node to prevent memory leak
        return nullptr; // No cycle detected
    }
    json final_ans = res_ptr->val; // Return the value of the node where the cycle begins
	std::unordered_set<ListNode*> visited_nodes;
	ListNode *temp = head;
	while (temp != nullptr) {
		visited_nodes.insert(temp);
		if (visited_nodes.contains(temp->next)) {
			temp->next = nullptr; // Break the cycle
			break;
		}
		temp = temp->next;
	}
	delete head; // Delete the head node to prevent memory leak
	// delete res_ptr;
	return final_ans;
}
