package problem1863

import (
	"encoding/json"
	"log"
	"strings"
)

func subsetXORSum(nums []int) int {
	/*
		XOR: each bit can be considered independently

		Suppose a bit is 1 in m numbers and 0 in n-m numbers
		The number of subsets with XOR 1 at this bit is:
		1. Choose one 1 and any subset of the n-m zeros -- Cm_1 * 2^(n-m)
		2. Choose three 1s and any subset of the n-m zeros -- Cm_3 * 2^(n-m)
		...
		2^(n-m) * (Cm_1 + Cm_3 + Cm_5 + ...)

		Since the sum of odd-sized binomial coefficients equals the sum of even-sized ones, this is equivalent to:
		2^(n-m) * 2^(m-1) = 2^(n-1)

		Each set bit therefore contributes 2^(n-1) times, giving the bitwise OR multiplied by 2^(n-1)
	*/
	or := 0
	for _, num := range nums {
		or |= num
	}
	return or << (len(nums) - 1)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return subsetXORSum(nums)
}
