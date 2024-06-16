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
private:
    ListNode *reverseList(ListNode *node) {
        if (node == nullptr || node->next == nullptr) {
            return node;
        }
        ListNode *new_head = reverseList(node->next);
        node->next->next = node;
        node->next = nullptr;
        return new_head;
    }

public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode *l1r = reverseList(l1), *l2r = reverseList(l2);
        auto dummy = new ListNode();
        ListNode *node = dummy;
        for (int cur = 0; l1r != nullptr || l2r != nullptr || cur != 0; node = node->next) {
            if (l1r != nullptr) {
                cur += l1r->val;
                l1r = l1r->next;
            }
            if (l2r != nullptr) {
                cur += l2r->val;
                l2r = l2r->next;
            }
            node->next = new ListNode(cur % 10);
            cur /= 10;
        }
        return reverseList(dummy->next);
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
    std::vector<int> l1_array = json::parse(inputArray.at(0));
    ListNode *l1 = IntArrayToListNode(l1_array);
    std::vector<int> l2_array = json::parse(inputArray.at(1));
    ListNode *l2 = IntArrayToListNode(l2_array);
    return ListNodeToIntArray(solution.addTwoNumbers(l1, l2));
}
