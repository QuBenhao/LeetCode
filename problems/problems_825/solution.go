package problem825

import (
	"encoding/json"
	"log"
	"strings"
)

func numFriendRequests(ages []int) (ans int) {
	/*
		ages[y] <= 0.5 * ages[x] + 7
		ages[y] > ages[x]
	*/
	cnts := make([]int, 121)
	for _, age := range ages {
		cnts[age]++
	}
	prefixSum := make([]int, 122)
	for i := 0; i < 121; i++ {
		prefixSum[i+1] = prefixSum[i] + cnts[i]
	}
	for age := 0; age < 121; age++ {
		left := age/2 + 7
		ans += max(0, cnts[age]*(prefixSum[age+1]-prefixSum[left+1]-1))
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var ages []int

	if err := json.Unmarshal([]byte(inputValues[0]), &ages); err != nil {
		log.Fatal(err)
	}

	return numFriendRequests(ages)
}
