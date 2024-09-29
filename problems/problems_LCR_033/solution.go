package problemLCR_033

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func groupAnagrams(strs []string) (ans [][]string) {
	mp := map[string][]string{}
	for _, str := range strs {
		s := []byte(str)
		sort.Slice(s, func(i, j int) bool { return s[i] < s[j] })
		sortedStr := string(s)
		mp[sortedStr] = append(mp[sortedStr], str)
	}
	for _, v := range mp {
		ans = append(ans, v)
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var strs []string

	if err := json.Unmarshal([]byte(inputValues[0]), &strs); err != nil {
		log.Fatal(err)
	}

	return groupAnagrams(strs)
}
