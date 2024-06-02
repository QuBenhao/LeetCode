//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool judgeCircle(string moves) {
        int horizontal = 0, vertical = 0;
        for (auto &c: moves) {
            switch (c) {
                case 'L':
                    horizontal--;
                    break;
                case 'R':
                    horizontal++;
                    break;
                case 'U':
                    vertical++;
                    break;
                default:
                    vertical--;
            }
        }
        return horizontal == 0 && vertical == 0;
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	int pos = input.find("\n");
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find("\n");
	}
	inputArray.push_back(input);

	Solution solution;
	string moves = json::parse(inputArray.at(0));
	return solution.judgeCircle(moves);
}
