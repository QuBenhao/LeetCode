package problem1871

import (
	"encoding/json"
	"log"
	"strings"
)

func canReach(s string, minJump int, maxJump int) bool {
	n := len(s)
	reachable := make([]bool, n)
	reachable[0] = true
	cnt := 0
	for i := 1; i < n; i++ {
		if i-minJump >= 0 && reachable[i-minJump] {
			cnt++
		}
		if i-maxJump-1 >= 0 && reachable[i-maxJump-1] {
			cnt--
		}
		reachable[i] = cnt > 0 && s[i] == '0'
	}
	return reachable[n-1]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var minJump int
	var maxJump int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &minJump); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &maxJump); err != nil {
		log.Fatal(err)
	}

	return canReach(s, minJump, maxJump)
}
