//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Skiplist {
public:
    Skiplist() {
        
    }
    
    bool search(int target) {
        
    }
    
    void add(int num) {
        
    }
    
    bool erase(int num) {
        
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
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
	auto obj0 = make_shared<Skiplist>();
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "search") {
			ans.push_back(obj0->search(op_values[i][0]));
			continue;
		}
		if (operators[i] == "add") {
			obj0->add(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "erase") {
			ans.push_back(obj0->erase(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
