package problem236

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
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil || root == p || root == q {
		return root
	}
	left := lowestCommonAncestor(root.Left, p, q)
	right := lowestCommonAncestor(root.Right, p, q)
	if left != nil && right != nil {
		return root
	} else if left != nil {
		return left
	}
	return right
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root, p, q *TreeNode

	var targetVal1 int
	if err := json.Unmarshal([]byte(inputValues[1]), &targetVal1); err != nil {
		log.Fatal(err)
	}
	var targetVal2 int
	if err := json.Unmarshal([]byte(inputValues[2]), &targetVal2); err != nil {
		log.Fatal(err)
	}
	nodes := ArrayToTreeAndTargets(inputValues[0], targetVal1, targetVal2)
	root, p, q = nodes[0], nodes[1], nodes[2]
	return TreeToArray(lowestCommonAncestor(root, p, q))
}
