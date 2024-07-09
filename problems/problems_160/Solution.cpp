//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/ListNode.h"
#include <vector>

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *pA = headA, *pB = headB;
        while (pA != pB) {
            pA = pA == nullptr ? headB : pA->next;
            pB = pB == nullptr ? headA : pB->next;
        }
        return pA;
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
    int iv = json::parse(inputArray.at(0));
    std::vector<int> headA_array = json::parse(inputArray.at(1));
    std::vector<int> headB_array = json::parse(inputArray.at(2));
    int idxA = json::parse(inputArray.at(3));
    int idxB = json::parse(inputArray.at(4));
    auto tp = IntArrayToIntersectionListNode(headA_array, headB_array, iv, idxA, idxB);
    ListNode *headA = get<0>(tp);
    ListNode *headB = get<1>(tp);

    auto result = solution.getIntersectionNode(headA, headB);
    return result != nullptr ? result->val : 0;
}
