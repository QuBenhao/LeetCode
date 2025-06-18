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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy = ListNode();
		ListNode *node = &dummy;
        while (list1 != nullptr or list2 != nullptr) {
            if (list2 != nullptr && (list1 == nullptr || list1->val > list2->val)) {
                node->next = new ListNode(list2->val);
                list2 = list2->next;
            } else if (list1 != nullptr) {
                node->next = new ListNode(list1->val);
                list1 = list1->next;
            }
            node = node->next;
        }
		ListNode *res = dummy.next;
		dummy.next = nullptr; // Disconnect the dummy node
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
	std::vector<int> list1_array = json::parse(inputArray.at(0));
	ListNode *list1 = IntArrayToListNode(list1_array);
	std::vector<int> list2_array = json::parse(inputArray.at(1));
	ListNode *list2 = IntArrayToListNode(list2_array);
	ListNode *res_ptr = solution.mergeTwoLists(list1, list2);
	json final_ans = ListNodeToIntArray(res_ptr);
	delete list1;
	delete list2;
	delete res_ptr;
	return final_ans;
}
