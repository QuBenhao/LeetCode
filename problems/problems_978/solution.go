package problem978

import (
	"encoding/json"
	"log"
	"strings"
)

func maxTurbulenceSize(arr []int) int {
	n := len(arr)
	ans := 1
	cur0, cur1 := 1, 1
	for i := 1; i < n; i++ {
		if arr[i] > arr[i-1] {
			cur1 = cur0 + 1
			cur0 = 1
		} else if arr[i] < arr[i-1] {
			cur0 = cur1 + 1
			cur1 = 1
		} else {
			cur0, cur1 = 1, 1
		}
		ans = max(ans, max(cur0, cur1))
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return maxTurbulenceSize(arr)
}
