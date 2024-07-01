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
    bool isPalindrome(ListNode* head) {
        vector<int> vals;
        for (ListNode* node = head; node != nullptr; node = node->next) {
            vals.push_back(node->val);
        }
        for (int left = 0, right = static_cast<int>(vals.size()) - 1; left < right; left++, right--) {
            if (vals[left] != vals[right]) {
                return false;
            }
        }
        return true;
    }
};

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	std::vector<int> head_array = json::parse(inputArray.at(0));
	ListNode *head = IntArrayToListNode(head_array);
	return solution.isPalindrome(head);
}
