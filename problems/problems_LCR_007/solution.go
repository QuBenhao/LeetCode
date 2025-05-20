package problemLCR_007

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func threeSum(nums []int) (ans [][]int) {
	sort.Ints(nums)
	n := len(nums)
	for i := 0; i < n-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		for left, right := i+1, n-1; left < right; {
			if sum := nums[i] + nums[left] + nums[right]; sum == 0 {
				ans = append(ans, []int{nums[i], nums[left], nums[right]})
				for left++; left < right && nums[left] == nums[left-1]; left++ {
				}
				for right--; left < right && nums[right] == nums[right+1]; right-- {
				}
			} else if sum < 0 {
				left++
			} else {
				right--
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return threeSum(nums)
}
