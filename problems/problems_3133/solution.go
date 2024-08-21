package problem3133

import (
	"encoding/json"
	"log"
	"strings"
)

func minEnd(n int, x int) int64 {
	n--
	ans := int64(x)
	for i, j := 0, 0; n>>j > 0; i++ {
		if (x>>i)&1 == 0 {
			ans |= int64((n>>j)&1) << i
			j++
		}
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &x); err != nil {
		log.Fatal(err)
	}

	return minEnd(n, x)
}
