package problem3145

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func sumE(k int) (res int) {
	var n, cnt1, sumI int
	for i := bits.Len(uint(k+1)) - 1; i > 0; i-- {
		c := cnt1<<i + i<<(i-1) // Number of additional exponents
		if c <= k {
			k -= c
			res += sumI<<i + i*(i-1)/2<<(i-1)
			sumI += i   // Sum of exponents for the ones already placed
			cnt1++      // Number of ones already placed
			n |= 1 << i // Place a 1
		}
	}
	// Handle the lowest bit separately
	if cnt1 <= k {
		k -= cnt1
		res += sumI
		n |= 1 // Set the lowest bit to 1
	}
	// Supply the remaining k exponents from the k lowest set bits of n
	for ; k > 0; k-- {
		res += bits.TrailingZeros(uint(n))
		n &= n - 1 // Clear the lowest set bit (set it to 0)
	}
	return
}

func findProductsOfElements(queries [][]int64) []int {
	ans := make([]int, len(queries))
	for i, q := range queries {
		er := sumE(int(q[1]) + 1)
		el := sumE(int(q[0]))
		ans[i] = pow(2, er-el, int(q[2]))
	}
	return ans
}

func pow(x, n, mod int) int {
	res := 1 % mod
	for ; n > 0; n /= 2 {
		if n%2 > 0 {
			res = res * x % mod
		}
		x = x * x % mod
	}
	return res
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var queries [][]int64

	if err := json.Unmarshal([]byte(inputValues[0]), &queries); err != nil {
		log.Fatal(err)
	}

	return findProductsOfElements(queries)
}
