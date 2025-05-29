//go:build ignore
#include "cpp/common/Solution.h"

#include <queue>

using namespace std;
using json = nlohmann::json;

class MovingAverage {
    int size;
    int64_t sum = 0;
    queue<int> q;
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {
        this->size = size;
        this->q = queue<int>();
        this->sum = 0;
    }
    
    double next(int val) {
        if (q.size() == size) {
            sum -= q.front();
            q.pop();
        }
        q.push(val);
        sum += val;
        return static_cast<double>(sum) / q.size();
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
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
	auto obj0 = make_shared<MovingAverage>(op_values[0][0]);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "next") {
			ans.push_back(obj0->next(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
