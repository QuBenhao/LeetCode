//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        if (combinationCheck(moves, 0)) {
            return "A";
        }
        if (combinationCheck(moves, 1)) {
            return "B";
        }
        return moves.size() < 9 ? "Pending" : "Draw";
    }

private:
    bool checkWin(vector<vector<int>>& moves, vector<int>& indexes) {
        bool meet = false;
        for (int i = 0; i < 4 && !meet; i++) {
            meet = true;
            for (auto idx: indexes) {
                if (i <= 1) {
                    if (moves[idx][i] != moves[indexes[0]][i]) {
                        meet = false;
                        break;
                    }
                } else if (i == 2) {
                    if (moves[idx][0] != moves[idx][1]) {
                        meet = false;
                        break;
                    }
                } else {
                    if (moves[idx][0] + moves[idx][1] != 2) {
                        meet = false;
                        break;
                    }
                }
            }
        }
        return meet;
    }

    bool combinationCheck(vector<vector<int>>& moves, int start) {
        for (int i = start; i < moves.size(); i += 2) {
            for (int j = i + 2; j < moves.size(); j += 2) {
                for (int k = j + 2; k < moves.size(); k += 2) {
                    vector<int> indexes = {i, j, k};
                    if (checkWin(moves, indexes)) {
                        return true;
                    }
                }
            }
        }
        return false;
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
	vector<vector<int>> moves = json::parse(inputArray.at(0));
	return solution.tictactoe(moves);
}
