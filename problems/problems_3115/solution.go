package problem3115

import (
	"encoding/json"
	"log"
	"strings"
)

func isPrime(n int) bool {
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return n >= 2
}

func maximumPrimeDifference(nums []int) int {
	left, right := 0, len(nums)-1
	for left < right && !isPrime(nums[left]) {
		left++
	}
	for left < right && !isPrime(nums[right]) {
		right--
	}
	return right - left
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maximumPrimeDifference(nums)
}
