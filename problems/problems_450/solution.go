package problem450

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
func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return nil
	}
	if key < root.Val {
		root.Left = deleteNode(root.Left, key)
	} else if key > root.Val {
		root.Right = deleteNode(root.Right, key)
	} else {
		if root.Left == nil {
			return root.Right
		} else if root.Right == nil {
			return root.Left
		}
		minNode := root.Right
		for minNode.Left != nil {
			minNode = minNode.Left
		}
		minNode.Right = deleteNode(root.Right, minNode.Val)
		minNode.Left = root.Left
		root = minNode
	}
	return root
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode
	var key int

	root = ArrayToTree(inputValues[0])
	if err := json.Unmarshal([]byte(inputValues[1]), &key); err != nil {
		log.Fatal(err)
	}

	return TreeToArray(deleteNode(root, key))
}
