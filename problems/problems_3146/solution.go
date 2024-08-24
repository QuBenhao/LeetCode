package problem3146

import (
	"encoding/json"
	"log"
	"strings"
)

func findPermutationDifference(s string, t string) (ans int) {
	idxes := make([]int, 26)
	for i := 0; i < len(s); i++ {
		idxes[s[i]-'a'] += i
		idxes[t[i]-'a'] -= i
	}
	for _, v := range idxes {
		if v < 0 {
			ans += -v
		} else {
			ans += v
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var t string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &t); err != nil {
		log.Fatal(err)
	}

	return findPermutationDifference(s, t)
}
