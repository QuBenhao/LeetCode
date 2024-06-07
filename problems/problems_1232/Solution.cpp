//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int xd = coordinates[1][0] - coordinates[0][0], yd = coordinates[1][1] - coordinates[0][1];
        int c = coordinates[0][0] * coordinates[1][1] - coordinates[0][1] * coordinates[1][0];
        for (int i = 2; i < coordinates.size(); i++) {
            auto x = coordinates[i][0], y = coordinates[i][1];
            if (x * yd - y * xd != c) {
                return false;
            }
        }
        return true;
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	vector<vector<int>> coordinates = json::parse(inputArray.at(0));
	return solution.checkStraightLine(coordinates);
}
