package problem1394

import (
	"encoding/json"
	"log"
	"strings"
)

func findLucky(arr []int) int {
	mapCount := make(map[int]int)
	for _, num := range arr {
		mapCount[num]++
	}
	ans := -1
	for num, count := range mapCount {
		if num == count && num > ans {
			ans = num
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return findLucky(arr)
}
