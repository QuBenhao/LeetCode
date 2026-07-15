package problem3867

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func gcdSum(nums []int) int64 {
	pg := make([]int, len(nums))
	mx := 0
	for i, x := range nums {
		if x > mx {
			mx = x
		}
		pg[i] = gcd(x, mx)
	}
	sort.Ints(pg)
	i, j := 0, len(pg)-1
	var ans int64
	for i < j {
		ans += int64(gcd(pg[i], pg[j]))
		i++
		j--
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return gcdSum(nums)
}
