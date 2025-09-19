//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Router {
public:
    Router(int memoryLimit) {
        
    }
    
    bool addPacket(int source, int destination, int timestamp) {
        
    }
    
    vector<int> forwardPacket() {
        
    }
    
    int getCount(int destination, int startTime, int endTime) {
        
    }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
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
	auto obj0 = make_unique<Router>(op_values[0][0]);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); ++i) {
		if (operators[i] == "addPacket") {
			ans.push_back(obj0->addPacket(op_values[i][0], op_values[i][1], op_values[i][2]));
			continue;
		}
		if (operators[i] == "forwardPacket") {
			ans.push_back(obj0->forwardPacket());
			continue;
		}
		if (operators[i] == "getCount") {
			ans.push_back(obj0->getCount(op_values[i][0], op_values[i][1], op_values[i][2]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
