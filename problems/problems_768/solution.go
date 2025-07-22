package problem768

import (
	"encoding/json"
	"log"
	"strings"
)

func maxChunksToSorted(arr []int) int {
	var st []int
	for _, num := range arr {
		if len(st) > 0 && num < st[len(st)-1] {
			mx := st[len(st)-1]
			for len(st) > 0 && num < st[len(st)-1] {
				st = st[:len(st)-1]
			}
			st = append(st, mx)
		} else {
			st = append(st, num)
		}
	}
	return len(st)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return maxChunksToSorted(arr)
}
