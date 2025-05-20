package problem2244

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumRounds(tasks []int) (ans int) {
	counter := map[int]int{}
	for _, v := range tasks {
		counter[v]++
	}
	for _, v := range counter {
		if v == 1 {
			return -1
		}
		switch v % 3 {
		case 1:
			ans += (v-4)/3 + 2
		case 2:
			ans += (v-2)/3 + 1
		default:
			ans += v / 3
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var tasks []int

	if err := json.Unmarshal([]byte(values[0]), &tasks); err != nil {
		log.Fatal(err)
	}

	return minimumRounds(tasks)
}
