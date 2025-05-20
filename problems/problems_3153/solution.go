package problem3153

import (
	"encoding/json"
	"log"
	"strings"
)

func sumDigitDifferences(nums []int) (ans int64) {
	length := 0
	for num := nums[0]; num > 0; num /= 10 {
		length++
	}
	counter := make([][]int64, length)
	for i := range counter {
		counter[i] = make([]int64, 10)
	}
	for i, num := range nums {
		for j := 0; num > 0; num /= 10 {
			ans += int64(i) - counter[j][num%10]
			counter[j][num%10]++
			j++
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

	return sumDigitDifferences(nums)
}
