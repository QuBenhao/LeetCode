package problem977

import (
	"encoding/json"
	"log"
	"strings"
)

func sortedSquares(nums []int) (ans []int) {
	n := len(nums)
	ans = make([]int, n)
	i, j, pos := 0, n-1, n-1
	for i <= j {
		if left, right := nums[i]*nums[i], nums[j]*nums[j]; left > right {
			ans[pos] = left
			i++
		} else {
			ans[pos] = right
			j--
		}
		pos--
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return sortedSquares(nums)
}
