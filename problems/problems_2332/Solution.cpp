//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int latestTimeCatchTheBus(vector<int>& buses, vector<int>& passengers, int capacity) {
      sort(buses.begin(), buses.end());
			sort(passengers.begin(), passengers.end());
			int n = static_cast<int>(passengers.size());
			int j = 0, c = 0;
			for (auto bus : buses) {
				c = capacity;
				while (c > 0 && j < n && passengers[j] <= bus) {
					j++;
					c--;
				}
			}
			j--;
			int ans = c > 0 ? buses.back() : passengers[j];
			while (j >= 0 && passengers[j] == ans) {
				j--;
				ans--;
			}
			return ans;
    }
};

json leetcode::qubh::Solve(string input_json_values) {
	vector<string> inputArray;
	size_t pos = input_json_values.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input_json_values.substr(0, pos));
		input_json_values = input_json_values.substr(pos + 1);
		pos = input_json_values.find('\n');
	}
	inputArray.push_back(input_json_values);

	Solution solution;
	vector<int> buses = json::parse(inputArray.at(0));
	vector<int> passengers = json::parse(inputArray.at(1));
	int capacity = json::parse(inputArray.at(2));
	return solution.latestTimeCatchTheBus(buses, passengers, capacity);
}
