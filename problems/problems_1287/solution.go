package problem1287

import (
	"encoding/json"
	"log"
	"strings"
)

func findSpecialInteger(arr []int) int {
	n := len(arr)
	for l, r := 0, 0; l < n; l = r {
		for r < n && arr[r] == arr[l] {
			r++
		}
		if (r-l)*4 > n {
			return arr[l]
		}
	}
	return -1
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return findSpecialInteger(arr)
}
