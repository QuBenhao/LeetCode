package problem2385

import (
	"encoding/json"
	. "leetCode/golang/models"
	"log"
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
func amountOfTime(root *TreeNode, start int) (ans int) {
	var dfs func(*TreeNode) (int, bool)
	dfs = func(node *TreeNode) (int, bool) {
		if node == nil {
			return 0, false
		}
		left, lf := dfs(node.Left)
		right, rf := dfs(node.Right)
		if node.Val == start {
			ans = max(left, right)
			return 0, true
		}
		d, found := 1, lf || rf
		if found {
			ans = max(ans, left+right+1)
			if lf {
				d += left
			} else {
				d += right
			}
		} else {
			d += max(left, right)
		}
		return d, found
	}
	dfs(root)
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode
	var start int

	root = ArrayToTree(inputValues[0])
	if err := json.Unmarshal([]byte(inputValues[1]), &start); err != nil {
		log.Fatal(err)
	}

	return amountOfTime(root, start)
}
