//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/ListNode.h"
#include <queue>

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
  ListNode *mergeKLists(vector<ListNode *> &lists) {
    auto cmp = [](ListNode *a, ListNode *b) { return a->val > b->val; };
    priority_queue<ListNode *, vector<ListNode *>, decltype(cmp)> pq;
    for (auto list : lists) {
      if (list) {
        pq.push(list);
      }
    }
    ListNode dummy = ListNode();
    ListNode *cur = &dummy;
    while (!pq.empty()) {
      auto node = pq.top();
      pq.pop();
      cur->next = node;
      cur = cur->next;
      if (node->next) {
        pq.push(node->next);
      }
    }
    cur = dummy.next;
    dummy.next = nullptr; // Disconnect the dummy node from the result
    return cur; // Return the merged list starting from the first real node
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
	std::vector<std::vector<int>> lists_arrays = json::parse(inputArray.at(0));
	auto lists = vector<ListNode*>(lists_arrays.size());
	for (size_t i = 0; i < lists.size(); ++i) {
		lists[i] = IntArrayToListNode(lists_arrays[i]);
	}
	ListNode *res_ptr = solution.mergeKLists(lists);
	json final_ans = ListNodeToIntArray(res_ptr);
	delete res_ptr;
	return final_ans;
}
