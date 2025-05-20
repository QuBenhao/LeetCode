package problemLCR_022

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
func detectCycle(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return nil
	}
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow, fast = slow.Next, fast.Next.Next
		if slow == fast {
			break
		}
	}
	if slow != fast {
		return nil
	}
	slow = head
	for slow != fast {
		if fast == nil {
			return nil
		}
		slow, fast = slow.Next, fast.Next
	}
	return slow
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var head *ListNode

	var headIntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	var headPos int
	if err := json.Unmarshal([]byte(inputValues[1]), &headPos); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedListCycle(headIntArray, headPos)

	res := detectCycle(head)
	if res == nil {
		return nil
	}
	return res.Val
}
