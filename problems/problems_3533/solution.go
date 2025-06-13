package problem3533

import (
	"encoding/json"
	"log"
	"math"
	"sort"
	"strings"
)

func concatenatedDivisibility(nums []int, k int) []int {
	n := len(nums)
	sort.Ints(nums)
	pow10 := make([]int, n)
	for i := range pow10 {
		pow10[i] = math.Pow10()
	}
	mask := 1 << n
	cache := make([][]bool, mask)
	for i := range cache {
		cache[i] = make([]bool, k)
	}
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return concatenatedDivisibility(nums, k)
}
