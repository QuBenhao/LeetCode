package problem3154

import (
	"encoding/json"
	"log"
	"strings"
)

const mx int = 31

var c [mx][mx]int

func init() {
	for i := 0; i < mx; i++ {
		c[i][0], c[i][i] = 1, 1
		for j := 1; j < i; j++ {
			c[i][j] = c[i-1][j] + c[i-1][j-1]
		}
	}
}

func waysToReachStair(k int) (ans int) {
	for j := 0; j < 30; j++ {
		if d := 1<<j - k; d >= 0 && d <= j+1 {
			ans += c[j+1][d]
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}

	return waysToReachStair(k)
}
