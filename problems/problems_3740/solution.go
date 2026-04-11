package problem3740

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minimumDistance(nums []int) int {
	ans := math.MaxInt
	record := make(map[int][]int)
	for k, num := range nums {
		record[num] = append(record[num], k)
		if len(record[num]) > 2 {
			i := record[num][len(record[num])-3]
			ans = min(ans, (k-i)*2)
		}
	}
	if ans == math.MaxInt {
		return -1
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minimumDistance(nums)
}
