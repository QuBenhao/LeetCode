package problem1717

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumGain(s string, x int, y int) (ans int) {
	var isA, isB func(int) bool
	if x < y {
		x, y = y, x
		isA = func(i int) bool { return s[i] == 'b' }
		isB = func(i int) bool { return s[i] == 'a' }
	} else {
		isA = func(i int) bool { return s[i] == 'a' }
		isB = func(i int) bool { return s[i] == 'b' }
	}
	n := len(s)
	for i := 0; i < n; {
		for i < n && !isA(i) && !isB(i) {
			i++
		}

		ca, cb := 0, 0
		for ; i < n && (isA(i) || isB(i)); i++ {
			if isA(i) {
				ca++
			} else {
				if ca > 0 {
					ans += x
					ca--
				} else {
					cb++
				}
			}
		}
		ans += min(ca, cb) * y
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var x int
	var y int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &x); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &y); err != nil {
		log.Fatal(err)
	}

	return maximumGain(s, x, y)
}
