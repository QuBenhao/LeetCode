package problem3606

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

var BUSINESS = map[string]int{
	"electronics": 0,
	"grocery":     1,
	"pharmacy":    2,
	"restaurant":  3,
}

func validateCoupons(code []string, businessLine []string, isActive []bool) (result []string) {
	var valids []int
	for i, c := range code {
		if !isActive[i] {
			continue
		}
		if _, ok := BUSINESS[businessLine[i]]; !ok {
			continue
		}
		if len(c) == 0 {
			continue
		}
		valid := true
		for _, char := range c {
			// check is alnumeric
			if !(('0' <= char && char <= '9') || ('A' <= char && char <= 'Z') || ('a' <= char && char <= 'z') || char == '_') {
				valid = false
				break
			}
		}
		if valid {
			valids = append(valids, i)
		}
	}
	sort.Slice(valids, func(i, j int) bool {
		b0, b1 := BUSINESS[businessLine[valids[i]]], BUSINESS[businessLine[valids[j]]]
		if b0 != b1 {
			return b0 < b1
		}
		return code[valids[i]] < code[valids[j]]
	})
	for _, idx := range valids {
		result = append(result, code[idx])
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var code []string
	var businessLine []string
	var isActive []bool

	if err := json.Unmarshal([]byte(inputValues[0]), &code); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &businessLine); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &isActive); err != nil {
		log.Fatal(err)
	}

	return validateCoupons(code, businessLine, isActive)
}
