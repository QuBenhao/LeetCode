package problem541

import (
	"encoding/json"
	"log"
	"strings"
)

func reverseStr(s string, k int) string {
	arr := []byte(s)
	n := len(s)
	for i := 0; i < n; i += 2 * k {
		for l, r := i, min(n-1, i+k-1); l < r; l++ {
			arr[l], arr[r] = arr[r], arr[l]
			r--
		}
	}
	return string(arr)
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

	return reverseStr(s, k)
}
