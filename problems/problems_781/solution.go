package problem781

import (
	"encoding/json"
	"log"
	"strings"
)

func numRabbits(answers []int) (ans int) {
	count := make(map[int]int)
	for _, v := range answers {
		if cnt, exist := count[v]; !exist || cnt%(v+1) == 0 {
			ans += v + 1
		}
		count[v]++
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var answers []int

	if err := json.Unmarshal([]byte(inputValues[0]), &answers); err != nil {
		log.Fatal(err)
	}

	return numRabbits(answers)
}
