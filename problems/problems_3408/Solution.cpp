//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class TaskManager {
public:
    TaskManager(vector<vector<int>>& tasks) {
        
    }
    
    void add(int userId, int taskId, int priority) {
        
    }
    
    void edit(int taskId, int newPriority) {
        
    }
    
    void rmv(int taskId) {
        
    }
    
    int execTop() {
        
    }
};

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager* obj = new TaskManager(tasks);
 * obj->add(userId,taskId,priority);
 * obj->edit(taskId,newPriority);
 * obj->rmv(taskId);
 * int param_4 = obj->execTop();
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
	auto obj0 = make_unique<TaskManager>(op_values[0][0]);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); ++i) {
		if (operators[i] == "add") {
			obj0->add(op_values[i][0], op_values[i][1], op_values[i][2]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "edit") {
			obj0->edit(op_values[i][0], op_values[i][1]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "rmv") {
			obj0->rmv(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "execTop") {
			ans.push_back(obj0->execTop());
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
