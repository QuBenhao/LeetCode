package models

import (
	"fmt"
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func ArrayToTree(input string) *TreeNode {
	input = strings.ReplaceAll(input, " ", "")
	if input[0] == '[' {
		input = input[1:]
	}
	if input[len(input)-1] == ']' {
		input = input[:len(input)-1]
	}
	if len(input) == 0 {
		return nil
	}
	splits := strings.Split(input, ",")
	var root *TreeNode
	if v, err := strconv.Atoi(splits[0]); err != nil {
		return nil
	} else {
		root = &TreeNode{Val: v}
	}
	isLeft := 1
	var nodes []*TreeNode
	currNode := root
	for i := 1; i < len(splits); i++ {
		if v, err := strconv.Atoi(splits[i]); err == nil {
			if isLeft == 1 {
				currNode.Left = &TreeNode{Val: v}
				nodes = append(nodes, currNode.Left)
			} else {
				currNode.Right = &TreeNode{Val: v}
				nodes = append(nodes, currNode.Right)
				currNode = nodes[0]
				nodes = nodes[1:]
			}
		}
		isLeft ^= 1
	}
	return root
}

func ArrayToTreeAndTarget(input string, target int) (*TreeNode, *TreeNode) {
	input = strings.ReplaceAll(input, " ", "")
	if input[0] == '[' {
		input = input[1:]
	}
	if input[len(input)-1] == ']' {
		input = input[:len(input)-1]
	}
	if len(input) == 0 {
		return nil, nil
	}
	splits := strings.Split(input, ",")
	var root, targetNode *TreeNode
	if v, err := strconv.Atoi(splits[0]); err != nil {
		return nil, nil
	} else {
		root = &TreeNode{Val: v}
		if v == target {
			targetNode = root
		}
	}
	isLeft := 1
	var nodes []*TreeNode
	currNode := root
	for i := 1; i < len(splits); i++ {
		if v, err := strconv.Atoi(splits[i]); err == nil {
			if isLeft == 1 {
				currNode.Left = &TreeNode{Val: v}
				if v == target {
					targetNode = currNode.Left
				}
				nodes = append(nodes, currNode.Left)
			} else {
				currNode.Right = &TreeNode{Val: v}
				if v == target {
					targetNode = currNode.Right
				}
				nodes = append(nodes, currNode.Right)
				currNode = nodes[0]
				nodes = nodes[1:]
			}
		}
		isLeft ^= 1
	}
	return root, targetNode
}

func TreeToArray(root *TreeNode) string {
	var ans []string
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		if node != nil {
			ans = append(ans, strconv.Itoa(node.Val))
			queue = append(queue, node.Left)
			queue = append(queue, node.Right)
		} else {
			ans = append(ans, "null")
		}
	}
	for len(ans) > 0 && ans[len(ans)-1] == "null" {
		ans = ans[:len(ans)-1]
	}
	return fmt.Sprintf("[%s]", strings.Join(ans, ", "))
}
