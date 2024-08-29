//go:build ignore
#include <sstream>
#include <string>
#include <vector>
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"


using namespace std;
using json = nlohmann::json;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
  // Encodes a tree to a single string.
  string serialize(TreeNode *root) {
    if (root == nullptr) {
      return "";
    }
    ostringstream out;
    function<void(TreeNode *)> dfs = [&](TreeNode *node) {
      if (node == nullptr) {
        out << "#,";
        return;
      }
      out << node->val << ",";
      dfs(node->left);
      dfs(node->right);
    };
    dfs(root);
    string result = out.str();
    // Remove trailing commas
    while (!result.empty() && (result.back() == ',' || result.back() == '#')) {
      result.pop_back();
    }
    return result;
  }

  // Decodes your encoded data to tree.
  TreeNode *deserialize(string data) {
    if (data.empty()) {
      return nullptr;
    }
    size_t pos = 0;
    function<TreeNode *()> dfs = [&]() -> TreeNode * {
      if (pos >= data.size()) {
        return nullptr;
      }
      if (data[pos] == '#') {
        pos += 2; // Skip over "#,"
        return nullptr;
      }
      int val = 0;
      int sign = 1;
      if (data[pos] == '-') {
        sign = -1;
        pos++;
      }
      while (pos < data.size() && data[pos] != ',') {
        val = val * 10 + data[pos] - '0';
        pos++;
      }

      pos++; // Skip over ","
      TreeNode *node = new TreeNode(val * sign);
      node->left = dfs();
      node->right = dfs();
      return node;
    };
    return dfs();
  }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));

json leetcode::qubh::Solve(string input_json_values) {
  vector<string> inputArray;
  size_t pos = input_json_values.find('\n');
  while (pos != string::npos) {
    inputArray.push_back(input_json_values.substr(0, pos));
    input_json_values = input_json_values.substr(pos + 1);
    pos = input_json_values.find('\n');
  }
  inputArray.push_back(input_json_values);
  vector<json> inputs = json::parse(inputArray.at(0));
  TreeNode *root = JsonArrayToTreeNode(inputs);

  Codec codec;
  string s = codec.serialize(root);
  TreeNode *ans = codec.deserialize(s);
  return TreeNodeToJsonArray(ans);
}
