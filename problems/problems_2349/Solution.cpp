//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class NumberContainers {
public:
    NumberContainers() {
        
    }
    
    void change(int index, int number) {
        
    }
    
    int find(int number) {
        
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
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
	auto obj0 = make_unique<NumberContainers>();
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); ++i) {
		if (operators[i] == "change") {
			obj0->change(op_values[i][0], op_values[i][1]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "find") {
			ans.push_back(obj0->find(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
