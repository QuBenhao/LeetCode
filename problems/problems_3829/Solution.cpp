//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class RideSharingSystem {
public:
    RideSharingSystem() {
        
    }
    
    void addRider(int riderId) {
        
    }
    
    void addDriver(int driverId) {
        
    }
    
    vector<int> matchDriverWithRider() {
        
    }
    
    void cancelRider(int riderId) {
        
    }
};

/**
 * Your RideSharingSystem object will be instantiated and called as such:
 * RideSharingSystem* obj = new RideSharingSystem();
 * obj->addRider(riderId);
 * obj->addDriver(driverId);
 * vector<int> param_3 = obj->matchDriverWithRider();
 * obj->cancelRider(riderId);
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
	auto obj0 = make_unique<RideSharingSystem>();
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); ++i) {
		if (operators[i] == "addRider") {
			obj0->addRider(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "addDriver") {
			obj0->addDriver(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "matchDriverWithRider") {
			ans.push_back(obj0->matchDriverWithRider());
			continue;
		}
		if (operators[i] == "cancelRider") {
			obj0->cancelRider(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
