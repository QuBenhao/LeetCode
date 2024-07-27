package problem49

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func groupAnagrams(strs []string) [][]string {
	group := map[string][]string{}
	for _, str := range strs {
		s := []byte(str)
		sort.Slice(s, func(i, j int) bool { return s[i] < s[j] })
		sortedStr := string(s)
		group[sortedStr] = append(group[sortedStr], str)
	}
	ans := make([][]string, 0, len(group))
	for _, v := range group {
		ans = append(ans, v)
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var strs []string

	if err := json.Unmarshal([]byte(inputValues[0]), &strs); err != nil {
		log.Fatal(err)
	}

	return groupAnagrams(strs)
}
