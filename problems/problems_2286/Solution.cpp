//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class BookMyShow {
public:
    BookMyShow(int n, int m) {

    }
    
    vector<int> gather(int k, int maxRow) {

    }
    
    bool scatter(int k, int maxRow) {

    }
};

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow* obj = new BookMyShow(n, m);
 * vector<int> param_1 = obj->gather(k,maxRow);
 * bool param_2 = obj->scatter(k,maxRow);
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
	auto obj0 = make_shared<BookMyShow>(op_values[0][0], op_values[0][1]);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "gather") {
			ans.push_back(obj0->gather(op_values[i][0], op_values[i][1]));
			continue;
		}
		if (operators[i] == "scatter") {
			ans.push_back(obj0->scatter(op_values[i][0], op_values[i][1]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
