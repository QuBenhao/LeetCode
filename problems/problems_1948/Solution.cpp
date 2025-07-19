//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

struct TrieNode {
    unordered_map<string, TrieNode*> son;
    string name; // 文件夹名称
    bool deleted = false; // 删除标记
};

class Solution {
public:
    vector<vector<string>> deleteDuplicateFolder(const vector<vector<string>>& paths) {
        TrieNode* root = new TrieNode();
        for (auto& path : paths) {
            // 把 path 插到字典树中，见 208. 实现 Trie
            TrieNode* cur = root;
            for (auto& s : path) {
                if (!cur->son.contains(s)) {
                    cur->son[s] = new TrieNode();
                }
                cur = cur->son[s];
                cur->name = s;
            }
        }

        unordered_map<string, TrieNode*> expr_to_node; // 子树括号表达式 -> 子树根节点

        auto gen_expr = [&](this auto&& gen_expr, TrieNode* node) -> string {
            if (node->son.empty()) { // 叶子
                return node->name; // 表达式就是文件夹名
            }

            vector<string> expr;
            for (auto& [_, son] : node->son) {
                // 每个子树的表达式外面套一层括号
                expr.emplace_back("(" + gen_expr(son) + ")");
            }
            ranges::sort(expr);

            string sub_tree_expr;
            for (auto& e : expr) {
                sub_tree_expr += e; // 按字典序拼接所有子树的表达式
            }

            if (expr_to_node.contains(sub_tree_expr)) { // 哈希表中有 sub_tree_expr，说明有重复的文件夹
                expr_to_node[sub_tree_expr]->deleted = true; // 哈希表中记录的节点标记为删除
                node->deleted = true; // 当前节点标记为删除
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

        // 在字典树上回溯，仅访问未被删除的节点，并将路径记录到答案中
        // 类似 257. 二叉树的所有路径
        auto dfs = [&](this auto&& dfs, TrieNode* node) -> void {
            if (node->deleted) {
                return;
            }
            path.push_back(node->name);
            ans.push_back(path);
            for (auto& [_, son] : node->son) {
                dfs(son);
            }
            path.pop_back(); // 恢复现场
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
