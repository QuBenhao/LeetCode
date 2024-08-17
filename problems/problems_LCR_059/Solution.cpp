//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {

    }
    
    int add(int val) {

    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
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
	auto obj0 = make_shared<KthLargest>(op_values[0][0], op_values[0][1]);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "add") {
			ans.push_back(obj0->add(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
