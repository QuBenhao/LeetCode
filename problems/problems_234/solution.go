package problem234

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
func isPalindrome(head *ListNode) bool {
	var vals []int
	for node := head; node != nil; node = node.Next {
		vals = append(vals, node.Val)
	}
	for left, right := 0, len(vals)-1; left < right; left++ {
		if vals[left] != vals[right] {
			return false
		}
		right--
	}
	return true
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var head *ListNode

	var headIntArray []int
	if err := json.Unmarshal([]byte(values[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedList(headIntArray)

	return isPalindrome(head)
}
