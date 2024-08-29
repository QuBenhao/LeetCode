package problemLCR_048

import (
	. "leetCode/golang/models"
	"strconv"
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

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	var ans []string
	var dfs func(*TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			ans = append(ans, "#")
			return
		}
		ans = append(ans, strconv.Itoa(node.Val))
		dfs(node.Left)
		dfs(node.Right)
	}
	dfs(root)
	for len(ans) > 0 && ans[len(ans)-1] == "#" {
		ans = ans[:len(ans)-1]
	}
	return strings.Join(ans, ",")
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}
	nodes := strings.Split(data, ",")
	var index int
	var dfs func() *TreeNode
	dfs = func() *TreeNode {
		if index == len(nodes) {
			return nil
		}
		if nodes[index] == "#" {
			index++
			return nil
		}
		val, _ := strconv.Atoi(nodes[index])
		index++
		node := &TreeNode{Val: val}
		node.Left = dfs()
		node.Right = dfs()
		return node
	}
	return dfs()
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	obj := Constructor()
	root := ArrayToTree(inputValues[0])
	serialize := obj.serialize(root)
	deserialize := obj.deserialize(serialize)
	return TreeToArray(deserialize)
}
