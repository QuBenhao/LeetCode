package problem1299

import (
	"encoding/json"
	"log"
	"strings"
)

func replaceElements(arr []int) []int {
	n := len(arr)
	maxValue := -1
	for i := n - 1; i >= 0; i-- {
		arr[i], maxValue = maxValue, max(maxValue, arr[i])
	}
	return arr
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return replaceElements(arr)
}
