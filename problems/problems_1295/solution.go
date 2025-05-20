package problem1295

import (
	"encoding/json"
	"log"
	"strings"
)

func findNumbers(nums []int) (ans int) {
	countDigits := func(n int) (count int) {
		for n > 0 {
			n /= 10
			count++
		}
		return
	}
	for _, num := range nums {
		if countDigits(num)%2 == 0 {
			ans++
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

	return findNumbers(nums)
}
