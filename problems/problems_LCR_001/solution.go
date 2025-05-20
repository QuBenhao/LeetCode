package problemLCR_001

import (
	"encoding/json"
	"log"
	"strings"
)

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func divide(a int, b int) (ans int) {
	if a == -1<<31 && b == -1 {
		return 1<<31 - 1
	}
	dividend, divisor := abs(a), abs(b)
	for i := 31; i >= 0; i-- {
		if d := divisor << i; d <= dividend {
			ans |= 1 << i
			dividend -= d
		}
	}
	if (a > 0) == (b > 0) {
		return ans
	}
	return -ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var a int
	var b int

	if err := json.Unmarshal([]byte(inputValues[0]), &a); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &b); err != nil {
		log.Fatal(err)
	}

	return divide(a, b)
}
