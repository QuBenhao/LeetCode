//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int takeCharacters(string s, int k) {
        int cnt[3]{};
        for (char c : s) {
            cnt[c - 'a']++; // 一开始，把所有字母都取走
        }
        if (cnt[0] < k || cnt[1] < k || cnt[2] < k) {
            return -1; // 字母个数不足 k
        }

        int mx = 0, left = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s[right] - 'a';
            cnt[c]--; // 移入窗口，相当于不取走 c
            while (cnt[c] < k) { // 窗口之外的 c 不足 k
                cnt[s[left] - 'a']++; // 移出窗口，相当于取走 s[left]
                left++;
            }
            mx = max(mx, right - left + 1);
        }
        return s.length() - mx;
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
	string s = json::parse(inputArray.at(0));
	int k = json::parse(inputArray.at(1));
	return solution.takeCharacters(s, k);
}
