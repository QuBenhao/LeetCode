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
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        // 最小距离来自相邻临界点，最大距离来自首尾临界点
        int first = 0, prev = 0, mn = INT_MAX;
        ListNode *a = head, *b = head->next, *c = head->next->next;
        for (int i = 2; c; ++i) {
            if (b->val > a->val && b->val > c->val || b->val < a->val && b->val < c->val) {
                if (prev) mn = min(mn, i - prev);
                else first = i;
                prev = i;
            }
            a = b, b = c, c = c->next;
        }
        return mn == INT_MAX ? vector<int>{-1, -1} : vector<int>{mn, prev - first};
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
	json final_ans = solution.nodesBetweenCriticalPoints(head);
	delete head;
	return final_ans;
}
