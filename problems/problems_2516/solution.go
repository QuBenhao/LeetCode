package problem2516

import (
	"encoding/json"
	"log"
	"strings"
)

func takeCharacters(s string, k int) int {
	cnt := [3]int{}
	for _, c := range s {
		cnt[c-'a']++ // Initially, take all characters
	}
	if cnt[0] < k || cnt[1] < k || cnt[2] < k {
		return -1 // Fewer than k occurrences of a character
	}

	mx, left := 0, 0
	for right, c := range s {
		c -= 'a'
		cnt[c]--         // Moving c into the window means leaving it untaken
		for cnt[c] < k { // Fewer than k occurrences of c remain outside the window
			cnt[s[left]-'a']++ // Moving s[left] out of the window means taking it
			left++
		}
		mx = max(mx, right-left+1)
	}
	return len(s) - mx
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return takeCharacters(s, k)
}
