//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
private:
    void addWordToAdj(const string& word, unordered_map<string, list<string>>& adj) {
        string copy = word;
        for (int i = 0; i < copy.size(); i++) {
            char oldChar = copy[i];
            copy[i] = '*';
            adj[word].push_back(copy);
            adj[copy].push_back(word);
            copy[i] = oldChar;
        }
    }

public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_map<string, list<string>> adj;

        // 填充无向图的邻接表
        for (const string& word : wordList) {
            addWordToAdj(word, adj);
        }
        addWordToAdj(beginWord, adj);

        if (adj.find(endWord) == adj.end()) {
            return 0;
        }

        // 存储一对各单词被初次转换时的距离，但源点终点处为 0，在最后调整
        unordered_map<string, int> dists1, dists2;
        dists1[beginWord] = 0;
        dists2[endWord] = 0;

        // 两个队列
        queue<string> q1, q2;
        q1.push(beginWord);
        q2.push(endWord);

        while (!q1.empty() && !q2.empty()) {
            // 找到周长小的一方
            queue<string>& q = q1.size() < q2.size() ? q1 : q2;
            unordered_map<string, int>& dists = q1.size() < q2.size() ? dists1 : dists2;
            // 确保遍历完一层
            for (int i = 0, size = q.size(); i < size; i++) {
                string word = q.front();
                q.pop();
                for (const string& nextWord : adj[word]) {
                    if (dists.find(nextWord) == dists.end()) {
                        dists[nextWord] = dists[word] + 1;
                        q.push(nextWord);
                        // 相交即刻返回
                        if (dists1.find(nextWord) != dists1.end() && dists2.find(nextWord) != dists2.end()) {
                            return (dists1[nextWord] + dists2[nextWord]) / 2 + 1;
                        }
                    }
                }
            }
        }

        return 0;
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
	string beginWord = json::parse(inputArray.at(0));
	string endWord = json::parse(inputArray.at(1));
	vector<string> wordList = json::parse(inputArray.at(2));
	return solution.ladderLength(beginWord, endWord, wordList);
}
