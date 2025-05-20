package problem389

import (
	"encoding/json"
	"log"
	"strings"
)

func findTheDifference(s string, t string) byte {
	ms, mt := map[byte]int{}, map[byte]int{}
	for i := 0; i < len(s); i++ {
		ms[s[i]]++
		mt[t[i]]++
	}
	mt[t[len(t)-1]]++
	for k, v := range mt {
		if val, ok := ms[k]; !ok || val < v {
			return k
		}
	}
	return 'x'
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string
	var t string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &t); err != nil {
		log.Fatal(err)
	}

	return findTheDifference(s, t)
}
