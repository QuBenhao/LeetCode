package problem2516

import (
	"encoding/json"
	"log"
	"strings"
)

func takeCharacters(s string, k int) int {
	cnt := [3]int{}
	for _, c := range s {
		cnt[c-'a']++ // 一开始，把所有字母都取走
	}
	if cnt[0] < k || cnt[1] < k || cnt[2] < k {
		return -1 // 字母个数不足 k
	}

	mx, left := 0, 0
	for right, c := range s {
		c -= 'a'
		cnt[c]--         // 移入窗口，相当于不取走 c
		for cnt[c] < k { // 窗口之外的 c 不足 k
			cnt[s[left]-'a']++ // 移出窗口，相当于取走 s[left]
			left++
		}
		mx = max(mx, right-left+1)
	}
	return len(s) - mx
}

func Solve(inputJsonValues string) interface{} {
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
