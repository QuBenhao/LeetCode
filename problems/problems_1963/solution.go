package problem1963

import (
	"encoding/json"
	"log"
	"strings"
)

func minSwaps(s string) (ans int) {
	cur := 0
	for _, r := range s {
		if r == '[' {
			cur++
		} else {
			cur--
			// 和最右边的[交换
			if cur < 0 {
				ans++
				cur = 1
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return minSwaps(s)
}
