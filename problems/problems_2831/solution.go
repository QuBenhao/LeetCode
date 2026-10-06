package problem2831

import (
	"encoding/json"
	"log"
	"strings"
)

func longestEqualSubarray(nums []int, k int) (ans int) {
	posLists := make([][]int, len(nums)+1)
	for i, x := range nums {
		posLists[x] = append(posLists[x], i-len(posLists[x]))
	}

	for _, pos := range posLists {
		if len(pos) <= ans {
			continue // Cannot increase ans
		}
		left := 0
		for right, p := range pos {
			for p-pos[left] > k { // Too many elements would need to be deleted
				left++
			}
			ans = max(ans, right-left+1)
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return longestEqualSubarray(nums, k)
}
