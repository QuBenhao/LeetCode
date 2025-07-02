package problem904

import (
	"encoding/json"
	"log"
	"strings"
)

func totalFruit(fruits []int) (ans int) {
	left := 0
	counts := make(map[int]int)
	for right, f := range fruits {
		counts[f]++
		for len(counts) > 2 {
			counts[fruits[left]]--
			if counts[fruits[left]] == 0 {
				delete(counts, fruits[left])
			}
			left++
		}
		ans = max(ans, right-left+1)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var fruits []int

	if err := json.Unmarshal([]byte(inputValues[0]), &fruits); err != nil {
		log.Fatal(err)
	}

	return totalFruit(fruits)
}
