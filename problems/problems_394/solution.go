package problem394

import (
	"encoding/json"
	"log"
	"strings"
)

func decodeString(s string) string {
	var stack [][]interface{}
	var res string
	var times int
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c == '[' {
			stack = append(stack, []interface{}{times, res})
			times, res = 0, ""
		} else if c == ']' {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			t, r := top[0].(int), top[1].(string)
			res = r + strings.Repeat(res, t)
		} else if c >= '0' && c <= '9' {
			times = times*10 + int(c-'0')
		} else {
			res += string(c)
		}
	}
	return res
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return decodeString(s)
}
