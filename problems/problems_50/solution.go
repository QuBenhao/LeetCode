package problem50

import (
	"encoding/json"
	"log"
	"strings"
)

func myPow(x float64, n int) float64 {
	if x == 0.0 {
		return 0.0
	}
	if n < 0 {
		x, n = 1.0/x, -n
	}
	ans := 1.0
	for n > 0 {
		if n&1 > 0 {
			ans *= x
		}
		x *= x
		n >>= 1
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var x float64
	var n int

	if err := json.Unmarshal([]byte(values[0]), &x); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &n); err != nil {
		log.Fatal(err)
	}

	return myPow(x, n)
}
