//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class NeighborSum {
public:
    NeighborSum(vector<vector<int>>& grid) {
        
    }
    
    int adjacentSum(int value) {
        
    }
    
    int diagonalSum(int value) {
        
    }
};

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum* obj = new NeighborSum(grid);
 * int param_1 = obj->adjacentSum(value);
 * int param_2 = obj->diagonalSum(value);
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
	auto obj0 = make_shared<NeighborSum>(op_values[0][0]);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "adjacentSum") {
			ans.push_back(obj0->adjacentSum(op_values[i][0]));
			continue;
		}
		if (operators[i] == "diagonalSum") {
			ans.push_back(obj0->diagonalSum(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
