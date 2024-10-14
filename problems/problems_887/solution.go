package problem887

import (
	"encoding/json"
	"log"
	"strings"
)

func superEggDrop(k, n int) int {
	f := make([]int, k+1)
	for i := 1; ; i++ {
		for j := k; j > 0; j-- {
			f[j] += f[j-1] + 1
		}
		if f[k] >= n {
			return i
		}
	}
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}

	return superEggDrop(k, n)
}
