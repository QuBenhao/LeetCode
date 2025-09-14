package problem3678

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func smallestAbsent(nums []int) int {
	used := make(map[int]bool)
	sm := 0
	mx := 0
	for _, num := range nums {
		used[num] = true
		sm += num
		mx = max(mx, num)
	}
	avg := int(math.Ceil(float64(sm+1) / float64(len(nums))))
	for i := max(avg, 1); i <= mx+1; i++ {
		if !used[i] {
			return i
		}
	}
	return 1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return smallestAbsent(nums)
}
