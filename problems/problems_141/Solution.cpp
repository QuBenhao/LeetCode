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
    bool hasCycle(ListNode *head) {
        if (head == nullptr) {
            return false;
        }
        auto slow = head, fast = head->next;
        while (slow != fast) {
            if (fast == nullptr || fast->next == nullptr) {
                return false;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
        return true;
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
	json final_ans = solution.hasCycle(head);
	std::unordered_set<ListNode*> visited_nodes;
	ListNode *temp = head;
	while (temp != nullptr) {
		visited_nodes.insert(temp);
		if (visited_nodes.find(temp->next) != visited_nodes.end()) {
			temp->next = nullptr; // Break the cycle
			break;
		}
		temp = temp->next;
	}
	delete head; // Delete the head node to prevent memory leak
	return final_ans;
}
