//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        double f = sqrt(candies * 2);
        int x = (int)(f + 1), s;
        for (s = x * (x + 1) / 2; s > candies; x--) {
            s -= x;
        }
        int remain = candies - s, d = x / num_people, m = x % num_people;
        vector<int> ans;
        for (int i = 0; i < num_people; i++) {
            ans.push_back((i + 1) * d + num_people * d * (d - 1) / 2);
            if (i < m) {
                ans[ans.size() - 1] += num_people * d + i + 1;
            }
        }
        ans[m] += remain;
        return ans;
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
	int candies = json::parse(inputArray.at(0));
	int num_people = json::parse(inputArray.at(1));
	return solution.distributeCandies(candies, num_people);
}
