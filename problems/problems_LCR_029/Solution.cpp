//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;

    Node() {}

    Node(int _val) {
        val = _val;
        next = NULL;
    }

    Node(int _val, Node* _next) {
        val = _val;
        next = _next;
    }
};
*/
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;

    Node() {}

    Node(int _val) {
        val = _val;
        next = NULL;
    }

    Node(int _val, Node* _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
public:
    Node* insert(Node* head, int insertVal) {
        Node* node = new Node(insertVal);
        if (head == nullptr) {
            node->next = node;
            head = node;
            return head;
        }
        Node* slow = head, *fast = head;
        do {
            if (slow->val <= insertVal && slow->next->val > insertVal) { // find insert
                node->next = slow->next;
                slow->next = node;
                return head;
            } else if (slow->val > slow->next->val) { // find start point
                if(slow->val <= insertVal || slow->next->val >= insertVal) {
                    node->next = slow->next;
                    slow->next = node;
                    return head;
                }
            }
            slow = slow->next;
            fast = fast->next->next;
        } while(slow != fast);
        // not find a place, insert at any place
        node->next = head->next;
        head->next = node;
        return head;
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
	int insertVal = json::parse(inputArray.at(1));
	return solution.insert(head, insertVal);
}
