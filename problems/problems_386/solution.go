package problem386

import (
	"encoding/json"
	"log"
	"strings"
)

func lexicalOrder(n int) (ans []int) {
	for i, j := 0, 1; i < n; i++ {
		ans = append(ans, j)
		if j*10 <= n {
			j *= 10
		} else {
			for j%10 == 9 || j+1 > n {
				j /= 10
			}
			j++
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

	return lexicalOrder(n)
}
