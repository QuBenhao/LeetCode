package problem2288

import (
	"encoding/json"
	"fmt"
	"log"
	"strings"
)

func discountPrices(sentence string, discount int) string {
	var ans []string
	for _, s := range strings.Split(sentence, " ") {
		if len(s) > 1 && s[0] == '$' {
			cur := 0
			for i := 1; i < len(s); i++ {
				if s[i] < '0' || s[i] > '9' {
					goto out
				}
				cur = 10*cur + int(s[i]-'0')
			}
			ans = append(ans, fmt.Sprintf("$%.2f", float64(100-discount)*float64(cur)/100.0))
			continue
		}
	out:
		ans = append(ans, s)
	}
	return strings.Join(ans, " ")
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var sentence string
	var discount int

	if err := json.Unmarshal([]byte(values[0]), &sentence); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &discount); err != nil {
		log.Fatal(err)
	}

	return discountPrices(sentence, discount)
}
