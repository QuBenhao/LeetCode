//go:build ignore
#include "cpp/common/Solution.h"
#include <iomanip>
#include <sstream>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string discountPrices(string sentence, int discount) {
        double d = 1 - discount / 100.0;
        stringstream ss(sentence);
        string ans, w;
        while (ss >> w) { // 一边分割，一边加到答案中
            if (!ans.empty()) {
                ans += ' ';
            }
            if (w.length() > 1 && w[0] == '$' && all_of(w.begin() + 1, w.end(), ::isdigit)) {
                stringstream s;
                s << fixed << setprecision(2) << '$' << static_cast<double>(stoll(w.substr(1))) * d;
                ans += s.str();
            } else {
                ans += w;
            }
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	string sentence = json::parse(inputArray.at(0));
	int discount = json::parse(inputArray.at(1));
	return solution.discountPrices(sentence, discount);
}
