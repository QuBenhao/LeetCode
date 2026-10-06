package problem1932

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
const mx int = 5e4 + 1

func canMerge(trees []*TreeNode) *TreeNode {
	isSub := [mx]bool{}      // For each root, determine whether it is a child in another BST
	roots := [mx]*TreeNode{} // For each child, find the BST root with the same value
	for _, rt := range trees {
		if rt.Left != nil {
			if isSub[rt.Left.Val] { // A BST cannot contain duplicate values, so trees cannot contain two child nodes with the same value
				return nil
			}
			isSub[rt.Left.Val] = true
		}
		if rt.Right != nil {
			if isSub[rt.Right.Val] {
				return nil
			}
			isSub[rt.Right.Val] = true
		}
		roots[rt.Val] = rt
	}

	var root *TreeNode
	for _, rt := range trees {
		if !isSub[rt.Val] { // The final root must not be a child of another BST, which would duplicate its value
			if root != nil { // There must be exactly one root; otherwise, the result is a forest
				return nil
			}
			root = rt
		}
	}
	if root == nil { // No root found
		return nil
	}

	cnt := 0
	// Validate the BST while constructing it
	var build func(*TreeNode, int, int) *TreeNode
	build = func(node *TreeNode, l, r int) *TreeNode {
		cnt++
		if node.Left != nil {
			if node.Left.Val <= l {
				return nil
			}
			if lo := roots[node.Left.Val]; lo != nil {
				node.Left = build(lo, l, node.Val)
				if node.Left == nil {
					return nil
				}
			}
		}
		if node.Right != nil {
			if node.Right.Val >= r {
				return nil
			}
			if ro := roots[node.Right.Val]; ro != nil {
				node.Right = build(ro, node.Val, r)
				if node.Right == nil {
					return nil
				}
			}
		}
		return node
	}
	root = build(root, 0, mx)
	if cnt == len(trees) { // Every trees[i] participates in the merged BST
		return root
	}
	return nil
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var trees []*TreeNode

	trees = ArrayToTreeArray(inputValues[0])

	return TreeToArray(canMerge(trees))
}
