//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>
#include <algorithm>


using namespace std;
using json = nlohmann::json;

class UnionFind {
    vector<int> parent;
    vector<int> size;
    int cc;
public:
    explicit UnionFind(int n): parent(n), size(n, 1), cc(n) {
        iota(parent.begin(), parent.end(), 0);
    }

    int Find(int x) {
        if (parent[x] != x) {
            parent[x] = Find(parent[x]); // Path compression
        }
        return parent[x];
    }

    bool Union(int x, int y) {
        int rootX = Find(x);
        int rootY = Find(y);
        if (rootX == rootY) return false; // Already connected

        int fa = min(rootX, rootY), child = max(rootX, rootY);
        parent[child] = fa; // Union by value
        size[fa] += size[child]; // Update size
        cc--; // Decrease connected components count
        return true;
    }
};

class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        UnionFind uf(26); // 26 lowercase letters
        for (size_t i = 0; i < s1.size(); ++i) {
            uf.Union(s1[i] - 'a', s2[i] - 'a');
        }

        string result;
        for (char c : baseStr) {
            int root = uf.Find(c - 'a');
            result += (char)(root + 'a'); // Convert back to character
        }

        return result;
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
	string s1 = json::parse(inputArray.at(0));
	string s2 = json::parse(inputArray.at(1));
	string baseStr = json::parse(inputArray.at(2));
	return solution.smallestEquivalentString(s1, s2, baseStr);
}
