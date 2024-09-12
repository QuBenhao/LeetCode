//go:build ignore
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
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class CBTInserter {
private:
	int n;
	TreeNode *root;
public:
  CBTInserter(TreeNode *root) {
		this->root = root;
		
	}

  int insert(int v) {}

  TreeNode *get_root() {}
};

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter* obj = new CBTInserter(root);
 * int param_1 = obj->insert(v);
 * TreeNode* param_2 = obj->get_root();
 */

json leetcode::qubh::Solve(string input_json_values) {
  vector<string> inputArray;
  size_t pos = input_json_values.find('\n');
  while (pos != string::npos) {
    inputArray.push_back(input_json_values.substr(0, pos));
    input_json_values = input_json_values.substr(pos + 1);
    pos = input_json_values.find('\n');
  }
  inputArray.push_back(input_json_values);

  vector<string> operators = json::parse(inputArray[0]);
  vector<vector<json>> op_values = json::parse(inputArray[1]);
  auto obj0 = make_shared<CBTInserter>(JsonArrayToTreeNode(op_values[0][0]));
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); i++) {
    if (operators[i] == "insert") {
      ans.push_back(obj0->insert(op_values[i][0]));
      continue;
    }
    if (operators[i] == "get_root") {
      ans.push_back(TreeNodeToJsonArray(obj0->get_root()));
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
