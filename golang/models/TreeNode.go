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

func InterfaceArrayToTree(input []any) *TreeNode {
	if len(input) == 0 {
		return nil
	}
	var root *TreeNode
	if input[0] == nil {
		return nil
	} else {
		root = &TreeNode{Val: int(input[0].(float64))}
	}
	isLeft := 1
	var nodes []*TreeNode
	currNode := root
	for i := 1; i < len(input); i++ {
		var node *TreeNode
		if input[i] == nil {
			node = nil
		} else {
			node = &TreeNode{Val: int(input[i].(float64))}
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

func ArrayToTree(input string) *TreeNode {
	var value any
	if err := json.Unmarshal([]byte(input), &value); err != nil {
		log.Fatalf("Unable to process tree input: %s", input)
		return nil
	}
	arr := value.([]any)
	return InterfaceArrayToTree(arr)
}

func ArrayToTreeArray(input string) []*TreeNode {
	var value []any
	if err := json.Unmarshal([]byte(input), &value); err != nil {
		log.Fatalf("Unable to process tree input: %s", input)
		return nil
	}
	if len(value) == 0 {
		return nil
	}
	var roots []*TreeNode
	for _, v := range value {
		arr := v.([]any)
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
	var value any
	if err := json.Unmarshal([]byte(input), &value); err != nil {
		log.Fatalf("Unable to process tree input: %s", input)
		return ans
	}
	arr := value.([]any)
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

func TreeToArray(root *TreeNode) []any {
	var ans []any
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

func TreeArrayToArray(roots []*TreeNode) []any {
	var ans []any
	for _, root := range roots {
		if root == nil {
			ans = append(ans, nil)
		} else {
			ans = append(ans, TreeToArray(root))
		}
	}
	return ans
}
