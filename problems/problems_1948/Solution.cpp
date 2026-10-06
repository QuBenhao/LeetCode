//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

struct TrieNode {
    unordered_map<string, TrieNode*> son;
    string name; // Folder name
    bool deleted = false; // Deletion flag
};

class Solution {
public:
    vector<vector<string>> deleteDuplicateFolder(const vector<vector<string>>& paths) {
        TrieNode* root = new TrieNode();
        for (auto& path : paths) {
            // Insert path into the trie; see 208. Implement Trie
            TrieNode* cur = root;
            for (auto& s : path) {
                if (!cur->son.contains(s)) {
                    cur->son[s] = new TrieNode();
                }
                cur = cur->son[s];
                cur->name = s;
            }
        }

        unordered_map<string, TrieNode*> expr_to_node; // Parenthesized subtree expression -> subtree root

        auto gen_expr = [&](this auto&& gen_expr, TrieNode* node) -> string {
            if (node->son.empty()) { // Leaf
                return node->name; // The expression is just the folder name
            }

            vector<string> expr;
            for (auto& [_, son] : node->son) {
                // Wrap each subtree expression in parentheses
                expr.emplace_back("(" + gen_expr(son) + ")");
            }
            ranges::sort(expr);

            string sub_tree_expr;
            for (auto& e : expr) {
                sub_tree_expr += e; // Concatenate all subtree expressions in lexicographic order
            }

            if (expr_to_node.contains(sub_tree_expr)) { // An existing sub_tree_expr in the map indicates duplicate folders
                expr_to_node[sub_tree_expr]->deleted = true; // Mark the node recorded in the map for deletion
                node->deleted = true; // Mark the current node for deletion
            } else {
                expr_to_node[sub_tree_expr] = node;
            }

            return node->name + sub_tree_expr;
        };

        for (auto& [_, son] : root->son) {
            gen_expr(son);
        }

        vector<vector<string>> ans;
        vector<string> path;

        // Backtrack through the trie, visiting only undeleted nodes and recording their paths in the answer
        // Similar to 257. Binary Tree Paths
        auto dfs = [&](this auto&& dfs, TrieNode* node) -> void {
            if (node->deleted) {
                return;
            }
            path.push_back(node->name);
            ans.push_back(path);
            for (auto& [_, son] : node->son) {
                dfs(son);
            }
            path.pop_back(); // Restore the previous state
        };

        for (auto& [_, son] : root->son) {
            dfs(son);
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
	vector<vector<string>> paths = json::parse(inputArray.at(0));
	return solution.deleteDuplicateFolder(paths);
}
