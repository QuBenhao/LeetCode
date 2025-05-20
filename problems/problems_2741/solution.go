package problem2741

import (
	"encoding/json"
	"log"
	"strings"
)

func specialPerm(nums []int) (ans int) {
	n := len(nums)
	u := 1<<n - 1
	f := make([][]int, u)
	for i := range f {
		f[i] = make([]int, n)
	}
	for i := range nums {
		f[0][i] = 1
	}
	for s := 1; s < u; s++ {
		for i, pre := range nums {
			if s>>i&1 != 0 {
				continue
			}
			for j, x := range nums {
				if s>>j&1 != 0 && (pre%x == 0 || x%pre == 0) {
					f[s][i] += f[s^(1<<j)][j]
				}
			}
		}
	}
	for i := range nums {
		ans += f[u^(1<<i)][i]
	}
	return ans % 1_000_000_007
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return specialPerm(nums)
}
