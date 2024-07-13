package problem53

import (
	"encoding/json"
	"log"
	"strings"
)

func maxSubArray(nums []int) int {
	var divAndConquer func(nums []int, left, right int) int
	divAndConquer = func(nums []int, left, right int) int {
		if left == right {
			return nums[left]
		}
		mid := left + (right-left)/2
		leftMax := divAndConquer(nums, left, mid)
		rightMax := divAndConquer(nums, mid+1, right)
		crossMax := 0
		leftCrossMax := nums[mid]
		rightCrossMax := nums[mid+1]
		for i := mid; i >= left; i-- {
			leftCrossMax = max(leftCrossMax, crossMax+nums[i])
			crossMax += nums[i]
		}
		crossMax = 0
		for i := mid + 1; i <= right; i++ {
			rightCrossMax = max(rightCrossMax, crossMax+nums[i])
			crossMax += nums[i]
		}
		return max(max(leftMax, rightMax), leftCrossMax+rightCrossMax)
	}
	return divAndConquer(nums, 0, len(nums)-1)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxSubArray(nums)
}
