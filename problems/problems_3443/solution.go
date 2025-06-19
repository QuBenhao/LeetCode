package problem3443

import (
	"encoding/json"
	"log"
	"strings"
)

func maxDistance(s string, k int) (ans int) {
	x, y := 0, 0
	k *= 2
	for i, r := range s {
		switch r {
		case 'N':
			y++
		case 'S':
			y--
		case 'E':
			x++
		case 'W':
			x--
		}
		ans = max(ans, min(i+1, k+abs(x)+abs(y)))
	}
	return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxDistance(s, k)
}
