//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int countPoints(string rings) {
      array<int, 10> count;
      for (int i = 0; i < rings.size(); i+=2) {
        count[rings[i+1] - '0'] |= 1 << "RGB".find(rings[i]);
      }
      int ans = 0;
      for (auto c : count) {
        if (c == (1 << 3) - 1) { // 111 in binary, meaning all three colors are present
          ans++;
        }
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
	string rings = json::parse(inputArray.at(0));
	return solution.countPoints(rings);
}
