package problem2024

import (
	"encoding/json"
	"log"
	"strings"
)

func maxConsecutiveAnswers(answerKey string, k int) (ans int) {
	n := len(answerKey)
	counter := map[byte]int{}
	for l, r := 0, 0; r < n; r++ {
		counter[answerKey[r]]++
		for min(counter['T'], counter['F']) > k {
			counter[answerKey[l]]--
			l++
		}
		ans = max(ans, r-l+1)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var answerKey string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &answerKey); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxConsecutiveAnswers(answerKey, k)
}
