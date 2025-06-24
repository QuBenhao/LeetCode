package problem891

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

const MOD = 1000000007

func sumSubseqWidths(nums []int) (ans int) {
	n := len(nums)
	sort.Ints(nums)
	powers := make([]int, n)
	powers[0] = 1
	for i := 1; i < n; i++ {
		powers[i] = (powers[i-1] * 2) % MOD
	}
	for i, num := range nums {
		ans = (ans + num*((powers[i]-powers[n-1-i]+MOD)%MOD)%MOD) % MOD
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return sumSubseqWidths(nums)
}
