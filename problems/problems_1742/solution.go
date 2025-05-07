package problem1742

import (
	"encoding/json"
	"log"
	"strings"
)

func countBalls(lowLimit int, highLimit int) (ans int) {
	convert := func(n int) (sum int) {
		for n > 0 {
			sum += n % 10
			n /= 10
		}
		return
	}
	counter := map[int]int{}
	for i := lowLimit; i <= highLimit; i++ {
		c := convert(i)
		counter[c]++
		if counter[c] > ans {
			ans = counter[c]
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var lowLimit int
	var highLimit int

	if err := json.Unmarshal([]byte(inputValues[0]), &lowLimit); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &highLimit); err != nil {
		log.Fatal(err)
	}

	return countBalls(lowLimit, highLimit)
}
