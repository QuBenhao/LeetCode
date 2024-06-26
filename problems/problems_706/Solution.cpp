//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>


using namespace std;
using json = nlohmann::json;

class MyHashMap {
private:
    unordered_map<int, int> map;
public:
    MyHashMap() {
        map = {};
    }
    
    void put(int key, int value) {
        map[key] = value;
    }
    
    int get(int key) {
        return map.find(key) == map.end() ? -1 : map[key];
    }
    
    void remove(int key) {
        map.erase(key);
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	vector<string> operators = json::parse(inputArray[0]);
	vector<vector<json>> values = json::parse(inputArray[1]);
	auto obj0 = make_shared<MyHashMap>();
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < values.size(); i++) {
		if (operators[i] == "put") {
			obj0->put(values[i][0], values[i][1]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "get") {
			ans.push_back(obj0->get(values[i][0]));
			continue;
		}
		if (operators[i] == "remove") {
			obj0->remove(values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
