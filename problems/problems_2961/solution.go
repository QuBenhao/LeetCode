package problem2961

import (
	"encoding/json"
	"log"
	"strings"
)

func getGoodIndices(variables [][]int, target int) (ans []int) {
	fastPowMod := func(a, b, mod int) int {
		res := 1
		for b > 0 {
			if b&1 == 1 {
				res = res * a % mod
			}
			a = a * a % mod
			b >>= 1
		}
		return res
	}
	for i, v := range variables {
		a, b, c, m := v[0], v[1], v[2], v[3]
		if fastPowMod(fastPowMod(a, b, 10), c, m) == target {
			ans = append(ans, i)
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var variables [][]int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &variables); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return getGoodIndices(variables, target)
}
