//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Allocator {
public:
    Allocator(int n) {
        
    }
    
    int allocate(int size, int mID) {
        
    }
    
    int freeMemory(int mID) {
        
    }
};

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator* obj = new Allocator(n);
 * int param_1 = obj->allocate(size,mID);
 * int param_2 = obj->freeMemory(mID);
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
	auto obj0 = make_shared<Allocator>(op_values[0][0]);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "allocate") {
			ans.push_back(obj0->allocate(op_values[i][0], op_values[i][1]));
			continue;
		}
		if (operators[i] == "freeMemory") {
			ans.push_back(obj0->freeMemory(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
