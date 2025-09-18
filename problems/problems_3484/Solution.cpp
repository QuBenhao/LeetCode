//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Spreadsheet {
public:
    Spreadsheet(int rows) {
        
    }
    
    void setCell(string cell, int value) {
        
    }
    
    void resetCell(string cell) {
        
    }
    
    int getValue(string formula) {
        
    }
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
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
	auto obj0 = make_unique<Spreadsheet>(op_values[0][0]);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); ++i) {
		if (operators[i] == "setCell") {
			obj0->setCell(op_values[i][0], op_values[i][1]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "resetCell") {
			obj0->resetCell(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "getValue") {
			ans.push_back(obj0->getValue(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
