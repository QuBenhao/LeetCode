#ifndef LEETCODECPP_TREENODE_H
#define LEETCODECPP_TREENODE_H

#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}

    ~TreeNode()
    {
        delete left;
        delete right;
    }
};

TreeNode *JsonArrayToTreeNode(json arr);
std::vector<TreeNode *> JsonArrayToTreeNodeArray(json arr);
json TreeNodeToJsonArray(TreeNode *root);

#endif //LEETCODECPP_TREENODE_H