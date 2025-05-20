package problem2239

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func findClosestNumber(nums []int) (ans int) {
	minDist := math.MaxInt
	for _, num := range nums {
		if num >= 0 {
			if num <= minDist {
				ans = num
				minDist = num
			}
		} else if -num < minDist {
			ans = num
			minDist = -num
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

	return findClosestNumber(nums)
}
