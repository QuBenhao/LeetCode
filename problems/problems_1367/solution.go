package problem1367

import (
	"encoding/json"
	. "leetCode/golang/models"
	"log"
	"strings"
)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubPath(head *ListNode, root *TreeNode) bool {
	var dfs func(*ListNode, *TreeNode) bool
	dfs = func(ln *ListNode, tn *TreeNode) bool {
		if ln == nil {
			return true
		}
		if tn == nil {
			return false
		}
		if tn.Val == ln.Val {
			if dfs(ln.Next, tn.Left) || dfs(ln.Next, tn.Right) {
				return true
			}
		}
		return ln == head && (dfs(ln, tn.Left) || dfs(ln, tn.Right))
	}
	return dfs(head, root)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var head *ListNode
	var root *TreeNode

	var headIntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedList(headIntArray)
	root = ArrayToTree(inputValues[1])

	return isSubPath(head, root)
}
