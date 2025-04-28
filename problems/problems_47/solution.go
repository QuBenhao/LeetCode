package problem47

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func NextPermutation(nums []int) {
	n := len(nums)
	i := n - 2
	for i >= 0 && nums[i] >= nums[i+1] {
		i--
	}
	for l, r := i+1, n-1; l < r; l, r = l+1, r-1 {
		nums[l], nums[r] = nums[r], nums[l]
	}
	if i < 0 {
		return
	}
	j := i + 1
	for j < n && nums[j] <= nums[i] {
		j++
	}
	nums[i], nums[j] = nums[j], nums[i]
}

func permuteUnique(nums []int) (ans [][]int) {
	// Sort the array to ensure we can skip duplicates
	sort.Ints(nums)
	ans = append(ans, append([]int{}, nums...))
	for {
		NextPermutation(nums)
		if sort.IntsAreSorted(nums) {
			break
		}
		ans = append(ans, append([]int{}, nums...))
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return permuteUnique(nums)
}
