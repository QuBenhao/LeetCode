//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Bank {
public:
    Bank(vector<long long>& balance) {
        
    }
    
    bool transfer(int account1, int account2, long long money) {
        
    }
    
    bool deposit(int account, long long money) {
        
    }
    
    bool withdraw(int account, long long money) {
        
    }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
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
	auto obj0 = make_unique<Bank>(op_values[0][0]);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); ++i) {
		if (operators[i] == "transfer") {
			ans.push_back(obj0->transfer(op_values[i][0], op_values[i][1], op_values[i][2]));
			continue;
		}
		if (operators[i] == "deposit") {
			ans.push_back(obj0->deposit(op_values[i][0], op_values[i][1]));
			continue;
		}
		if (operators[i] == "withdraw") {
			ans.push_back(obj0->withdraw(op_values[i][0], op_values[i][1]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
