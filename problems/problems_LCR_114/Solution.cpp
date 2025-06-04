//go:build ignore
#include "cpp/common/Solution.h"

#include <vector>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <sstream>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        unordered_map<char, unordered_set<char>> graph;
        unordered_map<char, int> inDegree;
        for (const string& word : words) {
            for (char c : word) {
                inDegree[c] = 0; // Initialize in-degree for each character
            }
        }

        for (int i = 0; i < words.size() - 1; ++i) {
            const string& word1 = words[i];
            const string& word2 = words[i + 1];
            int minLength = min(word1.size(), word2.size());
            bool foundDifference = false;

            for (int j = 0; j < minLength; ++j) {
                if (word1[j] != word2[j]) {
                    if (graph[word1[j]].insert(word2[j]).second) {
                        inDegree[word2[j]]++;
                    }
                    foundDifference = true;
                    break;
                }
            }

            if (!foundDifference && word1.size() > word2.size()) {
                return ""; // Invalid case: prefix condition
            }
        }

        queue<char> q;
        for (const auto& [c, degree] : inDegree) {
            if (degree == 0) {
                q.push(c);
            }
        }

        stringstream result;
        while (!q.empty()) {
            char c = q.front();
            q.pop();
            result << c;

            for (char neighbor : graph[c]) {
                if (--inDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        string order = result.str();
        return order.size() == inDegree.size() ? order : ""; // Check if all characters are included
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
	vector<string> words = json::parse(inputArray.at(0));
	return solution.alienOrder(words);
}
