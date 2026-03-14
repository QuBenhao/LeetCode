//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Fancy {
public:
    Fancy() {
        
    }
    
    void append(int val) {
        
    }
    
    void addAll(int inc) {
        
    }
    
    void multAll(int m) {
        
    }
    
    int getIndex(int idx) {
        
    }
};

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy* obj = new Fancy();
 * obj->append(val);
 * obj->addAll(inc);
 * obj->multAll(m);
 * int param_4 = obj->getIndex(idx);
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
	auto obj0 = make_unique<Fancy>();
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); ++i) {
		if (operators[i] == "append") {
			obj0->append(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "addAll") {
			obj0->addAll(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "multAll") {
			obj0->multAll(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "getIndex") {
			ans.push_back(obj0->getIndex(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
