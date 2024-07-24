#ifndef CPP_MODELS_TREENODE_H_
#define CPP_MODELS_TREENODE_H_

#include <vector>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using std::vector;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;

  TreeNode() : val(0), left(nullptr), right(nullptr) {}

  explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}

  ~TreeNode() {
    delete left;
    delete right;
  }
};

TreeNode *JsonArrayToTreeNode(json arr);
vector<TreeNode *> JsonArrayToTreeNodeWithTargets(json arr, vector<int> targets);
vector<TreeNode *> JsonArrayToTreeNodeArray(json arr);
json TreeNodeToJsonArray(TreeNode *root);

#endif  // CPP_MODELS_TREENODE_H_
