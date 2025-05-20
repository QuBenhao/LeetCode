package problem1535

import (
	"encoding/json"
	"log"
	"strings"
)

func getWinner(arr []int, k int) int {
	mx, win := arr[0], -1
	for _, v := range arr {
		if v > mx {
			mx = v
			win = 0
		}
		win++
		if win == k {
			break
		}
	}
	return mx
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var arr []int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &arr); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return getWinner(arr, k)
}
