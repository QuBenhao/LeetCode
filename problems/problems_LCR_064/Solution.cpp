//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class MagicDictionary {
public:
    /** Initialize your data structure here. */
    MagicDictionary() {

    }
    
    void buildDict(vector<string> dictionary) {

    }
    
    bool search(string searchWord) {

    }
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary* obj = new MagicDictionary();
 * obj->buildDict(dictionary);
 * bool param_2 = obj->search(searchWord);
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
	auto obj0 = make_shared<MagicDictionary>();
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "buildDict") {
			obj0->buildDict(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "search") {
			ans.push_back(obj0->search(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
