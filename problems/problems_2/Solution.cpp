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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        auto dummy = new ListNode(), node = dummy;
        for (int addition = 0; l1 != nullptr || l2 != nullptr || addition != 0; node = node->next) {
            int cur = addition;
            if (l1 != nullptr) {
                cur += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                cur += l2->val;
                l2 = l2->next;
            }
            node->next = new ListNode(cur % 10);
            addition = cur / 10;
        }
        return dummy->next;
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	auto pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	std::vector<int> l1_array = json::parse(inputArray.at(0));
	ListNode *l1 = IntArrayToListNode(l1_array);
	std::vector<int> l2_array = json::parse(inputArray.at(1));
	ListNode *l2 = IntArrayToListNode(l2_array);
	return ListNodeToIntArray(solution.addTwoNumbers(l1, l2));
}
