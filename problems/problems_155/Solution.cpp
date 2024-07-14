//go:build ignore
#include "cpp/common/Solution.h"
#include <stack>


using namespace std;
using json = nlohmann::json;

class MinStack {
private:
    stack<int> data;
    stack<int> helper;
public:
    MinStack() {
    }
    
    void push(int val) {
        data.push(val);
        if (helper.empty() || helper.top() >= val) {
            helper.push(val);
        } else {
            helper.push(helper.top());
        }
    }
    
    void pop() {
        data.pop();
        helper.pop();
    }
    
    int top() {
        return data.top();
    }
    
    int getMin() {
        return helper.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

json leetcode::qubh::Solve(string input_json_values) {
	vector<string> inputArray;
	size_t pos = input_json_values.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input_json_values.substr(0, pos));
		input_json_values = input_json_values.substr(pos + 1);
		pos = input_json_values.find('\n');
	}
	inputArray.push_back(input_json_values);

	vector<string> operators = json::parse(inputArray[0]);
	vector<vector<json>> op_values = json::parse(inputArray[1]);
	auto obj0 = make_shared<MinStack>();
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "push") {
			obj0->push(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "pop") {
			obj0->pop();
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "top") {
			ans.push_back(obj0->top());
			continue;
		}
		if (operators[i] == "getMin") {
			ans.push_back(obj0->getMin());
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
