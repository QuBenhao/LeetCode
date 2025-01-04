//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class ATM {
public:
    ATM() {
        
    }
    
    void deposit(vector<int> banknotesCount) {
        
    }
    
    vector<int> withdraw(int amount) {
        
    }
};

/**
 * Your ATM object will be instantiated and called as such:
 * ATM* obj = new ATM();
 * obj->deposit(banknotesCount);
 * vector<int> param_2 = obj->withdraw(amount);
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
	auto obj0 = make_shared<ATM>();
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "deposit") {
			obj0->deposit(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "withdraw") {
			ans.push_back(obj0->withdraw(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
