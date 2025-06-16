package problem3405

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD int = 1000000007

func fastPow(base int, exp int) int {
	result := 1
	base = base % MOD
	for exp > 0 {
		if exp%2 == 1 {
			result = (result * base) % MOD
		}
		exp = exp >> 1
		base = (base * base) % MOD
	}
	return result
}

func mathCombination(n int, k int) int {
	if k > n {
		return 0
	}
	if k == 0 || k == n {
		return 1
	}

	numerator := 1
	denominator := 1
	for i := 0; i < k; i++ {
		numerator = (numerator * (n - i)) % MOD
		denominator = (denominator * (i + 1)) % MOD
	}

	// Fermat's Little Theorem for modular inverse
	inverseDenominator := fastPow(denominator, MOD-2)
	return (numerator * inverseDenominator) % MOD
}

func countGoodArrays(n int, m int, k int) int {
	return m * fastPow(m-1, n-k-1) % MOD * mathCombination(n-1, k) % MOD
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var m int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return countGoodArrays(n, m, k)
}
