package problem1399

import (
	"encoding/json"
	"log"
	"strings"
)

func countLargestGroup(n int) (ans int) {
	counter := map[int]int{}
	mx := 0
	for i := 1; i <= n; i++ {
		s := 0
		for cur := i; cur > 0; cur /= 10 {
			s += cur % 10
		}
		counter[s]++
		if counter[s] > mx {
			ans = 1
			mx = counter[s]
		} else if counter[s] == mx {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return countLargestGroup(n)
}
