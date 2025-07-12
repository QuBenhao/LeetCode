package problem1900

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func earliestAndLatest(n, first, second int) []int {
	if first+second == n+1 {
		return []int{1, 1}
	}

	if first+second > n+1 {
		first, second = n+1-second, n+1-first
	}

	calcEarliestRounds := func(n int) int {
		res := 1

		if first+second <= (n+1)/2 {
			// 计算满足 first+second > ceil(n / 2^(k+1)) 的最小 k，推导过程见题解
			k := bits.Len(uint((n-1)/(first+second-1))) - 1
			n = (n-1)>>k + 1 // n = ceil(n / 2^k)
			res += k

			if second-first > 1 {
				return res + 1
			}
		}

		// 情况 1 和情况 3 合并，情况 2 合并到最后的 return
		if second-first == 1 || second > (n+1)/2 && second-first == 2 {
			// 先把 n 变成 ceil(n/2)，然后计算需要多少次 ceil(n/2) 的操作才能把 n 变成偶数，推导过程见题解
			// 这里把 (n+1)/2 和 n-1 合并，得到 (n+1)/2-1 = (n-1)/2
			return res + 1 + bits.TrailingZeros(uint((n-1)/2))
		}

		if second > (n+1)/2 && first%2 == 0 && first+second == n {
			res++
		}

		return res + 1
	}

	earliest := calcEarliestRounds(n)
	latest := min(bits.Len(uint(n-1)), n+1-second)
	return []int{earliest, latest}
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var firstPlayer int
	var secondPlayer int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &firstPlayer); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &secondPlayer); err != nil {
		log.Fatal(err)
	}

	return earliestAndLatest(n, firstPlayer, secondPlayer)
}
