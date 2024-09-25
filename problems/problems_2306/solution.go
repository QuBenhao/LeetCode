package problem2306

import (
	"encoding/json"
	"log"
	"strings"
)

func distinctNames(ideas []string) (ans int64) {
	group := [26]map[string]bool{}
	for i := range group {
		group[i] = map[string]bool{}
	}
	for _, s := range ideas {
		group[s[0]-'a'][s[1:]] = true // 按照首字母分组
	}

	for i, a := range group { // 枚举所有组对
		for _, b := range group[:i] {
			m := 0 // 交集的大小
			for s := range a {
				if b[s] {
					m++
				}
			}
			ans += int64(len(a)-m) * int64(len(b)-m)
		}
	}
	return ans * 2 // 乘 2 放到最后
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var ideas []string

	if err := json.Unmarshal([]byte(inputValues[0]), &ideas); err != nil {
		log.Fatal(err)
	}

	return distinctNames(ideas)
}
