package problem687

import (
	. "leetCode/golang/models"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func longestUnivaluePath(root *TreeNode) (ans int) {
	var dfs func(*TreeNode) int
	dfs = func(tn *TreeNode) int {
		if tn == nil {
			return 0
		}
		curAns, cur, left, right := 0, 0, dfs(tn.Left), dfs(tn.Right)
		if tn.Left != nil && tn.Left.Val == tn.Val {
			curAns = left + 1
			cur += left + 1
		}
		if tn.Right != nil && tn.Right.Val == tn.Val {
			curAns = max(curAns, right+1)
			cur += right + 1
		}
		ans = max(ans, cur)
		return curAns
	}
	dfs(root)
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode

	root = ArrayToTree(inputValues[0])

	return longestUnivaluePath(root)
}
