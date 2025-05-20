package problem503

import (
	"encoding/json"
	"log"
	"strings"
)

func nextGreaterElements(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	var stack []int
	for i := 0; i < 2*n; i++ {
		if i < n {
			ans[i] = -1
		}
		for d := len(stack) - 1; d >= 0 && nums[stack[d]] < nums[i%n]; d-- {
			ans[stack[d]] = nums[i%n]
			stack = stack[:d]
		}
		if i < n {
			stack = append(stack, i)
		} else if len(stack) == 0 {
			break
		}
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return nextGreaterElements(nums)
}
