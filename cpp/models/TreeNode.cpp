#include "TreeNode.h"
#include <queue>


TreeNode *JsonArrayToTreeNode(json arr)
{
    if (arr.empty())
    {
        return nullptr;
    }
    TreeNode *root = new TreeNode(arr[0]);
    int isLeft = true;
    std::queue<TreeNode *> q;
   TreeNode *curr_node = root;
   for (int i = 1; i < arr.size(); i++)
   {
       json num = arr[i];
       if (isLeft == 1)
       {
           if (num != nullptr)
           {
               curr_node->left = new TreeNode(int(num));
               q.push(curr_node->left);
           }
       }
       else
       {
           if (num != nullptr)
           {
               curr_node->right = new TreeNode(int(num));
               q.push(curr_node->right);
           }
           curr_node = q.front();
           q.pop();
       }
       isLeft ^= 1;
   }
}

json TreeNodeToJsonArray(TreeNode *root)
{
    json ans = json::array();
    std::queue<TreeNode *> q;
    q.push(root);
    while (!q.empty())
    {
        TreeNode *node = q.front();
        q.pop();
        ans.push_back(node->val);
        if (node)
        {
            q.push(node->left);
            q.push(node->right);
        }
    }
    while (!ans.empty() && ans.back() == nullptr)
    {
        ans.erase(ans.end() - 1);
    }
    return ans;
}