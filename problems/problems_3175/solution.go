package problem3175

import (
	"encoding/json"
	"log"
	"strings"
)

func findWinningPlayer(skills []int, k int) (ans int) {
	for i, cur := 1, 0; i < len(skills); i++ {
		if skills[i] < skills[ans] {
			cur++
		} else {
			cur = 1
			ans = i
		}
		if cur == k {
			break
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var skills []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &skills); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return findWinningPlayer(skills, k)
}
