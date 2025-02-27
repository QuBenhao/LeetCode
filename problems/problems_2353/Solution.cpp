//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class FoodRatings {
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        
    }
    
    void changeRating(string food, int newRating) {
        
    }
    
    string highestRated(string cuisine) {
        
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
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
	vector<int> ratings_array = op_values[0][2].get<vector<int>>();
	auto obj0 = make_shared<FoodRatings>(op_values[0][0], op_values[0][1], ratings_array);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "changeRating") {
			obj0->changeRating(op_values[i][0], op_values[i][1]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "highestRated") {
			ans.push_back(obj0->highestRated(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
