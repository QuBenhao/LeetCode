package problem3583

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD = 1_000_000_007

func specialTriplets(nums []int) (ans int) {
	sufCount := map[int]int{}
	for _, num := range nums {
		sufCount[num]++
	}
	preCount := map[int]int{}
	for _, num := range nums {
		sufCount[num]--
		ans = (ans + preCount[num*2]*sufCount[num*2]) % MOD
		preCount[num]++
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return specialTriplets(nums)
}
