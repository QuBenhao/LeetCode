package problem230

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
func kthSmallest(root *TreeNode, k int) int {
	var nums []int
	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		nums = append(nums, node.Val)
		inorder(node.Right)
	}
	inorder(root)
	return nums[k-1]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode
	var k int

	root = ArrayToTree(inputValues[0])
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return kthSmallest(root, k)
}
