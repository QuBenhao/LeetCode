package problems.problems_1932;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import qubhjava.models.TreeNode;

public class Solution extends BaseSolution {
    // 森林中叶子节点的度数，下标是叶子节点的值
    public int[] du = new int[50005];
    // 根节点的值对应的根节点
    public TreeNode[] nodeValToNode = new TreeNode[50005];
    // 拓扑排序的队列
    public Queue<TreeNode> queue = new LinkedList<>();
    // 森林中树的棵数
    public int n;
    // 合并次数，即森林中树减少的数量
    public int sub = 0;
    // 合并完成的树是否满足二叉搜索树
    public boolean isOK = true;
    public TreeNode canMerge(List<TreeNode> trees) {
        n = trees.size();
        for (int i = 0; i < n; i++) {
            TreeNode treeNode = trees.get(i);
            nodeValToNode[treeNode.val] = treeNode;
            // 该根节点的叶子节点度数增加操作
            dfs(treeNode , true);
        }
        queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            TreeNode treeNode = trees.get(i);
            // 根节点度数为0，入队
            if(du[treeNode.val] == 0) {
                queue.add(treeNode);
            }
        }
        // 只有根节点度数为0的根节点数量为1个时，才有可能合并成一个满足要求的二叉搜索树
        // 大于1个时很容易理解为什么不行，因为肯定不能合并成一棵树
        // 根节点度数为0，即该根节点不可能“附属”到其他树上，只能作为根，就是多根情况，很显然不行
        // 等于0个时，为什么不行？因为有循环，合并成的树不可能符合二叉搜索树的要求
        // 如1 -> 2 , 2 -> 3 , 3 -> 1（a -> b代表根节点a的叶子节点中有和根节点b相同的值）
        // 如果合并根节点1、2得到新树（根节点还是1），新树不能与根节点3合并，因为根节点3中的叶子节点有和根节点1相同的值
        // 这样不满足二叉搜索树的要求（任意节点的左子树中的值都严格小于此节点的值、任意节点的右子树中的值都严格大于此节点的值）
        if(queue.size() != 1) return null;
        // 记录合并后的整棵树的根节点，就是答案
        TreeNode ans = queue.peek();
        while (!queue.isEmpty()) {
            TreeNode treeNode = queue.poll();
            // 该根节点的叶子节点度数减少操作
            dfsSub(treeNode);
            // 已经合并完成了，可以退出了
            if(sub == n - 1) break;
        }
        // 拓扑排序结束了，合并还没有完成
        if(sub != n - 1) return null;
        // 检查合并完成的树是否满足要求
        check(ans);
        if(!isOK) return null;
        // 满足要求
        return ans;
    }

    // 拓扑排序，叶子节点的度数++ , 如果根节点就是叶子节点则不需要++，因为根节点想要入队（度数为0时），只会根据其他树的叶子节点来--
    public void dfs(TreeNode treeNode , boolean isRoot) {
        if(treeNode.left == null && treeNode.right == null) {
            if(!isRoot) du[treeNode.val]++;
            return;
        }
        if(treeNode.left != null) dfs(treeNode.left , false);
        if(treeNode.right != null) dfs(treeNode.right , false);
    }

    // 拓扑排序，叶子节点的度数-- ，如果叶子节点此时的度数为0，并且该叶子节点与某个根节点的值相同，就合并树，并且把该根节点加入队列
    public void dfsSub(TreeNode treeNode) {
        if(treeNode.left == null && treeNode.right == null) {
            du[treeNode.val]--;
            if(du[treeNode.val] == 0 && nodeValToNode[treeNode.val] != null) {
                // 合并树
                treeNode.left = nodeValToNode[treeNode.val].left;
                treeNode.right = nodeValToNode[treeNode.val].right;
                // 度数为0了，可以入队了
                queue.add(treeNode);
                // 森林中树--
                sub++;
            }
            return;
        }
        if(treeNode.left != null) dfsSub(treeNode.left);
        if(treeNode.right != null) dfsSub(treeNode.right);
    }

    // 检查合并的树是否满足二叉搜索树，返回该子树的{最小值 ， 最大值}
    public int[] check(TreeNode treeNode) {
        // 已经不满足要求了，随便返回什么
        if (!isOK) return new int[2];
        int[] minAndMax = new int[2];
        // 初值
        minAndMax[0] = treeNode.val;  // 最小值
        minAndMax[1] = treeNode.val;  // 最大值
        if (treeNode.left != null) {
            int[] left = check(treeNode.left);
            // 更新
            minAndMax[0] = Math.min(minAndMax[0], left[0]);
            minAndMax[1] = Math.max(minAndMax[1], left[1]);
            // 如果节点值不大于左子树的最大值，则不满足要求
            if (treeNode.val <= left[1]) isOK = false;
        }
        if (treeNode.right != null) {
            int[] right = check(treeNode.right);
            // 更新
            minAndMax[0] = Math.min(minAndMax[0], right[0]);
            minAndMax[1] = Math.max(minAndMax[1], right[1]);
            // 如果节点值不小于右子树的最小值，则不满足要求
            if (treeNode.val >= right[0]) isOK = false;
        }
        return minAndMax;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<TreeNode> trees = jsonArrayToTreeNodeList(inputJsonValues[0]);
        return JSON.toJSON(TreeNode.TreeNodeToArray(canMerge(trees)));
    }
}
