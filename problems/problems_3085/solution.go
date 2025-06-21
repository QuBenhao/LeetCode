package problem3085

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func minimumDeletions(word string, k int) int {
	counter := make([]int, 26)
	for _, char := range word {
		counter[char-'a']++
	}
	sort.Ints(counter)
	ans := len(word)
	for i, v := range counter {
	    if i > 0 && counter[i-1] == v {
	        continue
	    }
		cur, maxV := 0, v+k
		for j := range i {
			if counter[j] >= v {
				break
			}
			cur += counter[j]
		}
		for j := 25; j > i; j-- {
			if counter[j] <= maxV {
				break
			}
			cur += counter[j] - maxV
		}
		ans = min(ans, cur)
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &word); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return minimumDeletions(word, k)
}
