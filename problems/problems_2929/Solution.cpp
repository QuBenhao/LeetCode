//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
    long long c2(long long n) {
        return n > 1 ? (n-1) * n / 2 : 0;
    }
public:
    long long distributeCandies(int n, int limit) {
        /*
         * Distribute n candies among 3 people, with no one receiving more than limit
         * Place two separators among n+2 positions
         * Inclusion-exclusion: all ways - C_{3}^{1} * ways with at least one person above limit + C_{3}^{2} * ways with at least two above limit - ways with all three above limit
         * All ways: C_{n+2}_{2}
         * At least one person exceeds limit: C_{n+2-(limit+1)}_{2}
         * At least two people exceed limit: C_{n+2-2*(limit+1)}_{2}
         * At least three people exceed limit: C_{n+2-3*(limit+1)}_{2}
        */
        return c2(n+2) - 3*c2(n+1-limit) + 3 * c2(n-2*limit) - c2(n-1-3*limit);
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
	int n = json::parse(inputArray.at(0));
	int limit = json::parse(inputArray.at(1));
	return solution.distributeCandies(n, limit);
}
