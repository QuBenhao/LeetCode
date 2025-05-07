package problem1534

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func countGoodTriplets(arr []int, a int, b int, c int) (ans int) {
	n := len(arr)
	for i := range n - 2 {
		for j := i + 1; j < n-1; j++ {
			if math.Abs(float64(arr[i]-arr[j])) > float64(a) {
				continue
			}
			for k := j + 1; k < n; k++ {
				if math.Abs(float64(arr[j]-arr[k])) > float64(b) {
					continue
				}
				if math.Abs(float64(arr[i]-arr[k])) > float64(c) {
					continue
				}
				ans++
			}
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int
	var a int
	var b int
	var c int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &a); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &b); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &c); err != nil {
		log.Fatal(err)
	}

	return countGoodTriplets(arr, a, b, c)
}
