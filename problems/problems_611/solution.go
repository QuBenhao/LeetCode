package problem611

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func triangleNumber(nums []int) (ans int) {
	sort.Ints(nums)
	for i, num := range nums {
		for j, k := i-1, 0; k < j; j-- {
			for k < j && nums[j]+nums[k] <= num {
				k++
			}
			ans += j - k
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

	return triangleNumber(nums)
}
