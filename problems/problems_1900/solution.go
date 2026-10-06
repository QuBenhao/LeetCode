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
			// Compute the smallest k satisfying first+second > ceil(n / 2^(k+1)); see the solution for the derivation
			k := bits.Len(uint((n-1)/(first+second-1))) - 1
			n = (n-1)>>k + 1 // n = ceil(n / 2^k)
			res += k

			if second-first > 1 {
				return res + 1
			}
		}

		// Combine cases 1 and 3; include case 2 in the final return
		if second-first == 1 || second > (n+1)/2 && second-first == 2 {
			// First replace n with ceil(n/2), then count how many ceil(n/2) operations make n even; see the solution for the derivation
			// Combine (n+1)/2 and n-1 to get (n+1)/2-1 = (n-1)/2
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
