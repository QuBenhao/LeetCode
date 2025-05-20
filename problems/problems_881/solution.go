package problem881

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func numRescueBoats(people []int, limit int) (ans int) {
	sort.Ints(people)
	for left, right := 0, len(people)-1; left <= right; right-- {
		if people[left]+people[right] <= limit {
			left++
		}
		ans++
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var people []int
	var limit int

	if err := json.Unmarshal([]byte(values[0]), &people); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &limit); err != nil {
		log.Fatal(err)
	}

	return numRescueBoats(people, limit)
}
