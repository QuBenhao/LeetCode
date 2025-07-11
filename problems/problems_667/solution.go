package problem667

import (
	"encoding/json"
	"log"
	"strings"
)

func constructArray(n int, k int) (ans []int) {
	for i := range k + 1 {
		if i%2 == 0 {
			ans = append(ans, i/2+1)
		} else {
			ans = append(ans, k-i/2+1)
		}
	}
	for i := k + 2; i <= n; i++ {
		ans = append(ans, i)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return constructArray(n, k)
}
