package problem623

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
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
	if depth == 1 {
		return &TreeNode{Val: val, Left: root}
	}
	var dfs func(*TreeNode, int)
	dfs = func(node *TreeNode, currentDepth int) {
		if node == nil {
			return
		}
		if currentDepth == depth-1 {
			node.Left = &TreeNode{Val: val, Left: node.Left}
			node.Right = &TreeNode{Val: val, Right: node.Right}
		} else {
			dfs(node.Left, currentDepth+1)
			dfs(node.Right, currentDepth+1)
		}
	}
	dfs(root, 1)
	return root
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode
	var val int
	var depth int

	root = ArrayToTree(inputValues[0])
	if err := json.Unmarshal([]byte(inputValues[1]), &val); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &depth); err != nil {
		log.Fatal(err)
	}

	return TreeToArray(addOneRow(root, val, depth))
}
