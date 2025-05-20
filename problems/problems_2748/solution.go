package problem2748

import (
	"encoding/json"
	"log"
	"strings"
)

func countBeautifulPairs(nums []int) (ans int) {
	cnts := make([]int, 10)
	for _, num := range nums {
		cur := num % 10
		for i, c := range cnts {
			if c > 0 && gcd(cur, i) == 1 {
				ans += c
			}
		}
		for num >= 10 {
			num /= 10
		}
		cnts[num]++
	}
	return
}

func gcd(a, b int) int {
	for a != 0 {
		a, b = b%a, a
	}
	return b
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countBeautifulPairs(nums)
}
