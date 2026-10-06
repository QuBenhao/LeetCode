package problem3086

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minimumMoves(nums []int, k, maxChanges int) int64 {
	pos := []int{}
	c := 0 // Length of consecutive ones in nums
	for i, x := range nums {
		if x == 0 {
			continue
		}
		pos = append(pos, i) // Record the positions of ones
		c = max(c, 1)
		if i > 0 && nums[i-1] == 1 {
			if i > 1 && nums[i-2] == 1 {
				c = 3 // There are 3 consecutive ones
			} else {
				c = max(c, 2) // There are 2 consecutive ones
			}
		}
	}

	c = min(c, k)
	if maxChanges >= k-c {
		// Each of the remaining k-c ones can be obtained in two operations
		return int64(max(c-1, 0) + (k-c)*2)
	}

	n := len(pos)
	sum := make([]int, n+1)
	for i, x := range pos {
		sum[i+1] = sum[i] + x
	}

	ans := math.MaxInt
	// maxChanges ones can each be obtained in two operations; the rest must be moved to pos[i] one step at a time
	size := k - maxChanges
	for right := size; right <= n; right++ {
		// s1+s2 is the sum of distances from every pos[j], for j in [left, right), to pos[(left+right)/2]
		left := right - size
		i := left + size/2
		s1 := pos[i]*(i-left) - (sum[i] - sum[left])
		s2 := sum[right] - sum[i] - pos[i]*(right-i)
		ans = min(ans, s1+s2)
	}
	return int64(ans + maxChanges*2)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int
	var maxChanges int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &maxChanges); err != nil {
		log.Fatal(err)
	}

	return minimumMoves(nums, k, maxChanges)
}
