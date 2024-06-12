package problem2813

import (
	"encoding/json"
	"log"
	"strings"
)

func findMaximumElegance(items [][]int, k int) int64 {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var items [][]int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &items); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return findMaximumElegance(items, k)
}
