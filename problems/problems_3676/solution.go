package problem3676

import (
	"encoding/json"
	"log"
	"strings"
)

func bowlSubarrays(nums []int) int64 {
	n := len(nums)
	leftGreater := make([]int, n)
	rightGreater := make([]int, n)
	for i := range n {
		leftGreater[i] = -1
		rightGreater[i] = -1
	}
	var st []int
	for i, num := range nums {
		for len(st) > 0 && nums[st[len(st)-1]] < num {
			rightGreater[st[len(st)-1]] = i
			st = st[:len(st)-1]
		}
		if len(st) > 0 {
			leftGreater[i] = st[len(st)-1]
		}
		st = append(st, i)
	}
	s := map[int]bool{}
	for i := range n {
		if leftGreater[i] != -1 && rightGreater[i] != -1 {
			s[leftGreater[i]*n+rightGreater[i]] = true
		}
	}
	return int64(len(s))
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return bowlSubarrays(nums)
}
