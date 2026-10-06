package problem368

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func largestDivisibleSubset(nums []int) (ans []int) {
	sort.Ints(nums)
	n := len(nums)
	// f[i] is the length of the longest divisible subset ending at the ith number among the numbers considered so far.
	f := make([]int, n)
	// g[i] records the predecessor index used to obtain f[i]: if f[i] = f[j] + 1, then g[i] = j.
	g := make([]int, n)

	for i := 0; i < n; i++ {
		// The subset contains at least the number itself, so start with length 1 and itself as the predecessor
		l := 1
		prev := i
		for j := 0; j < i; j++ {
			if nums[i]%nums[j] == 0 {
				// If this number can extend a longer sequence, update the maximum length and predecessor
				if f[j]+1 > l {
					l = f[j] + 1
					prev = j
				}
			}
		}

		// Record the final length and predecessor
		f[i] = l
		g[i] = prev
	}

	// Scan all f[i] values to find the maximum length and its index
	max := -1
	idx := -1
	for i := 0; i < n; i++ {
		if f[i] > max {
			idx = i
			max = f[i]
		}
	}

	// Reconstruct the subset by following g[]
	for len(ans) != max {
		ans = append(ans, nums[idx])
		idx = g[idx]
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	res := largestDivisibleSubset(nums)
	sort.Ints(res)
	return res
}
