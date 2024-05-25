package problem1738

import (
	"encoding/json"
	"log"
	"strings"
)

func kthLargestValue(matrix [][]int, k int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var matrix [][]int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &matrix); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return kthLargestValue(matrix, k)
}
