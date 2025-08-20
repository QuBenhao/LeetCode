package problem652

import (
	"fmt"
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
func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
	cache, resCache := make(map[string]*TreeNode), make(map[string]*TreeNode)
	var dfs func(node *TreeNode) string
	dfs = func(node *TreeNode) string {
		if node == nil {
			return "#"
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		curr := fmt.Sprintf("%d,%s,%s", node.Val, left, right)
		if _, ok := cache[curr]; ok {
			if _, exists := resCache[curr]; !exists {
				resCache[curr] = node
			}
		}
		cache[curr] = node
		return curr
	}
	dfs(root)
	var res []*TreeNode
	for _, v := range resCache {
		res = append(res, v)
	}
	return res
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode

	root = ArrayToTree(inputValues[0])

	return TreeArrayToArray(findDuplicateSubtrees(root))
}
