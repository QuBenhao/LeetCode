package problemLCR_080

import (
	"encoding/json"
	"log"
	"strings"
)

func combine(n int, k int) (ans [][]int) {
	var backtrack func(int, []int)
	backtrack = func(cur int, path []int) {
		if len(path) == k {
			ans = append(ans, append([]int(nil), path...))
			return
		}
		for i := cur; i <= n; i++ {
			path = append(path, i)
			backtrack(i+1, path)
			path = path[:len(path)-1]
		}
	}
	backtrack(1, []int{})
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return combine(n, k)
}
