package problem658

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func findClosestElements(arr []int, k int, x int) []int {
	right, _ := slices.BinarySearch(arr, x)
	left := right - 1
	n := len(arr)
	x <<= 1
	for k > 0 && left >= 0 && right < n {
		if arr[left]+arr[right] >= x {
			left--
		} else {
			right++
		}
		k--
	}
	if k > 0 {
		if left < 0 {
			right += k
		} else {
			left -= k
		}
	}
	return arr[left+1 : right]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int
	var k int
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &x); err != nil {
		log.Fatal(err)
	}

	return findClosestElements(arr, k, x)
}
