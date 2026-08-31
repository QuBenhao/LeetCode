package problem2058

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
func nodesBetweenCriticalPoints(head *ListNode) []int {
	// 最小距离来自相邻临界点，最大距离来自首尾临界点
	first, prev, mn := 0, 0, 1<<30
	a, b, c := head, head.Next, head.Next.Next
	for i := 2; c != nil; i++ {
		if b.Val > a.Val && b.Val > c.Val || b.Val < a.Val && b.Val < c.Val {
			if prev > 0 {
				mn = min(mn, i-prev)
			} else {
				first = i
			}
			prev = i
		}
		a, b, c = b, c, c.Next
	}
	if mn == 1<<30 {
		return []int{-1, -1}
	}
	return []int{mn, prev - first}
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var head *ListNode

	var headIntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedList(headIntArray)

	return nodesBetweenCriticalPoints(head)
}
