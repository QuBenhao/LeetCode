package problem3170

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func clearStars(s string) string {
	bytes := []byte(s)
	stack := make([][]int, 26)
	mask := 0
	for i, b := range bytes {
		if b == '*' {
			k := bits.TrailingZeros(uint(mask))
			st := stack[k]
			bytes[st[len(st)-1]] = '*'
			stack[k] = st[:len(st)-1]
			if len(stack[k]) == 0 {
				mask &= ^(1 << k)
			}
		} else {
			k := b - 'a'
			stack[k] = append(stack[k], i)
			mask |= 1 << k
		}
	}
	var t []byte
	for _, b := range bytes {
		if b != '*' {
			t = append(t, b)
		}
	}
	return string(t)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return clearStars(s)
}
