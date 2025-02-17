//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class RangeFreqQuery {
public:
    RangeFreqQuery(vector<int>& arr) {
        
    }
    
    int query(int left, int right, int value) {
        
    }
};

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery* obj = new RangeFreqQuery(arr);
 * int param_1 = obj->query(left,right,value);
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
	vector<int> arr_array = op_values[0][0].get<vector<int>>();
	auto obj0 = make_shared<RangeFreqQuery>(arr_array);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "query") {
			ans.push_back(obj0->query(op_values[i][0], op_values[i][1], op_values[i][2]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
