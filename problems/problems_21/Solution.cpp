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
        ListNode* dummy = new ListNode(), *node = dummy;
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
        return dummy->next;
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	std::vector<int> list1_array = json::parse(inputArray.at(0));
	ListNode *list1 = IntArrayToListNode(list1_array);
	std::vector<int> list2_array = json::parse(inputArray.at(1));
	ListNode *list2 = IntArrayToListNode(list2_array);
	return ListNodeToIntArray(solution.mergeTwoLists(list1, list2));
}
