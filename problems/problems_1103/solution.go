package problem1103

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func distributeCandies(candies int, num_people int) []int {
	// (x + 2)^2 > (x + 2) * (x + 1) > 2 * candies >= x * (x + 1) > x^2
	f := math.Sqrt(float64(candies * 2))
	x := int(f + 1)
	var s int
	for s = x * (x + 1) / 2; s > candies; x-- {
		s -= x
	}
	remain := candies - s
	div, mod := x/num_people, x%num_people
	ans := make([]int, num_people)
	for i := 0; i < num_people; i++ {
		ans[i] += (i+1)*div + num_people*div*(div-1)/2
		if i < mod {
			ans[i] += num_people*div + i + 1
		}
	}
	ans[mod] += remain
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var candies int
	var num_people int

	if err := json.Unmarshal([]byte(values[0]), &candies); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &num_people); err != nil {
		log.Fatal(err)
	}

	return distributeCandies(candies, num_people)
}
