package problemLCR_053

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
func inorderSuccessor(root *TreeNode, p *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Val <= p.Val {
		return inorderSuccessor(root.Right, p)
	}
	left := inorderSuccessor(root.Left, p)
	if left != nil {
		return left
	}
	return root
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode
	var p *TreeNode

	var targetVal1 int
	if err := json.Unmarshal([]byte(inputValues[1]), &targetVal1); err != nil {
		log.Fatal(err)
	}
	nodes := ArrayToTreeAndTargets(inputValues[0], targetVal1)
	root, p = nodes[0], nodes[1]

	return TreeToArray(inorderSuccessor(root, p))
}
