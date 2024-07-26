package models

import (
	"encoding/json"
	"log"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func ArrayToTree(input string) *TreeNode {
	var value interface{}
	if err := json.Unmarshal([]byte(input), &value); err != nil {
		log.Fatalf("Unable to process tree input: %s", input)
		return nil
	}
	arr := value.([]interface{})
	if len(arr) == 0 {
		return nil
	}
	var root *TreeNode
	if arr[0] == nil {
		return nil
	} else {
		root = &TreeNode{Val: int(arr[0].(float64))}
	}
	isLeft := 1
	var nodes []*TreeNode
	currNode := root
	for i := 1; i < len(arr); i++ {
		var node *TreeNode
		if arr[i] == nil {
			node = nil
		} else {
			node = &TreeNode{Val: int(arr[i].(float64))}
		}
		if isLeft == 1 {
			if node != nil {
				currNode.Left = node
				nodes = append(nodes, currNode.Left)
			}
		} else {
			if node != nil {
				currNode.Right = node
				nodes = append(nodes, currNode.Right)
			}
			currNode = nodes[0]
			nodes = nodes[1:]
		}
		isLeft ^= 1
	}
	return root
}

func ArrayToTreeArray(input string) []*TreeNode {
	var value []interface{}
	if err := json.Unmarshal([]byte(input), &value); err != nil {
		log.Fatalf("Unable to process tree input: %s", input)
		return nil
	}
	if len(value) == 0 {
		return nil
	}
	var roots []*TreeNode
	for _, v := range value {
		arr := v.([]interface{})
		if len(arr) == 0 {
			roots = append(roots, nil)
			continue
		}
		var root *TreeNode
		if arr[0] == nil {
			root = nil
		} else {
			root = &TreeNode{Val: int(arr[0].(float64))}
		}
		isLeft := 1
		var nodes []*TreeNode
		currNode := root
		for i := 1; i < len(arr); i++ {
			var node *TreeNode
			if arr[i] == nil {
				node = nil
			} else {
				node = &TreeNode{Val: int(arr[i].(float64))}
			}
			if isLeft == 1 {
				if node != nil {
					currNode.Left = node
					nodes = append(nodes, currNode.Left)
				}
			} else {
				if node != nil {
					currNode.Right = node
					nodes = append(nodes, currNode.Right)
				}
				currNode = nodes[0]
				nodes = nodes[1:]
			}
			isLeft ^= 1
		}
		roots = append(roots, root)
	}
	return roots
}

func ArrayToTreeAndTargets(input string, targets ...int) []*TreeNode {
	targetNums := len(targets)
	ans := make([]*TreeNode, 1+targetNums)
	for i := 0; i <= targetNums; i++ {
		ans[i] = nil
	}
	var value interface{}
	if err := json.Unmarshal([]byte(input), &value); err != nil {
		log.Fatalf("Unable to process tree input: %s", input)
		return ans
	}
	arr := value.([]interface{})
	if len(arr) == 0 {
		return ans
	}
	var root *TreeNode
	if arr[0] == nil {
		return ans
	} else {
		root = &TreeNode{Val: int(arr[0].(float64))}
		ans[0] = root
		for i, target := range targets {
			if target == root.Val {
				ans[i+1] = root
			}
		}
	}
	isLeft := 1
	var nodes []*TreeNode
	currNode := root
	for i := 1; i < len(arr); i++ {
		var node *TreeNode
		if arr[i] == nil {
			node = nil
		} else {
			node = &TreeNode{Val: int(arr[i].(float64))}
			for j, target := range targets {
				if target == node.Val {
					ans[j+1] = node
				}
			}
		}
		if isLeft == 1 {
			if node != nil {
				currNode.Left = node
				nodes = append(nodes, currNode.Left)
			}
		} else {
			if node != nil {
				currNode.Right = node
				nodes = append(nodes, currNode.Right)
			}
			currNode = nodes[0]
			nodes = nodes[1:]
		}
		isLeft ^= 1
	}
	return ans
}

func TreeToArray(root *TreeNode) []interface{} {
	var ans []interface{}
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		if node != nil {
			ans = append(ans, node.Val)
			queue = append(queue, node.Left)
			queue = append(queue, node.Right)
		} else {
			ans = append(ans, nil)
		}
	}
	for len(ans) > 0 && ans[len(ans)-1] == nil {
		ans = ans[:len(ans)-1]
	}
	return ans
}
