//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool isRobotBounded(string instructions) {
        int x = 0, y = 0, d = 0;
        int dirs[4][2] = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
        for (int i = 0; i < instructions.length(); i++) {
            switch (instructions[i]) {
                case 'L':
                    d = (d + 1) % 4;
                    break;
                case 'R':
                    d = (d + 3) % 4;
                    break;
                default:
                    x += dirs[d][0];
                    y += dirs[d][1];
            }
        }
        return (x == 0 && y == 0) || d != 0;
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
	string instructions = json::parse(inputArray.at(0));
	return solution.isRobotBounded(instructions);
}
