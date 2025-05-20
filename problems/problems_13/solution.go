package problem13

import (
	"encoding/json"
	"log"
	"strings"
)

func romanToInt(s string) int {
	romanMap := map[byte]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	ans := romanMap[s[0]]
	for i := 1; i < len(s); i++ {
		if ld, sd := romanMap[s[i-1]], romanMap[s[i]]; ld < sd {
			ans += sd - 2*ld
		} else {
			ans += sd
		}
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return romanToInt(s)
}
