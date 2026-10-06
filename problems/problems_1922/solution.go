package problem1922

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD = 1000_000_007

func fastPower(a, b, mod int64) int {
	result := int64(1)
	a = a % mod // Apply the initial modulus if mod > 0
	for b > 0 {
		if b%2 == 1 { // The current binary digit is 1
			result = (result * a) % mod
		}
		a = (a * a) % mod // Square the base
		b /= 2            // Shift right by one bit
	}
	return int(result)
}

func countGoodNumbers(n int64) (ans int) {
	// 0, 2, 4, 6, 8
	// 2, 3, 5, 7
	ans = fastPower(int64(20), n/2, MOD)
	if n%2 == 1 {
		ans = (ans * 5) % MOD
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int64

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return countGoodNumbers(n)
}
