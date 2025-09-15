package problem2197

import (
	"encoding/json"
	"log"
	"strings"
)

func replaceNonCoprimes(nums []int) (ans []int) {
	for _, num := range nums {
		for len(ans) > 0 {
			g := gcd(num, ans[len(ans)-1])
			if g == 1 {
				break
			}
			num = ans[len(ans)-1] / g * num
			ans = ans[:len(ans)-1]
		}
		ans = append(ans, num)
	}
	return
}

func gcd(a, b int) int {
	for a != 0 {
		a, b = b%a, a
	}
	return b
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return replaceNonCoprimes(nums)
}
