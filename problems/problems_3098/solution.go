package problem3098

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

const mod = 1e9 + 7
const inf = 0x3f3f3f3f

func sumOfPowers(nums []int, k int) int {
	n := len(nums)
	sort.Ints(nums)

	var vals []int
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			vals = append(vals, nums[i]-nums[j])
		}
	}
	vals = append(vals, inf)
	sort.Ints(vals)
	vals = unique(vals)

	d := make([][][]int, n)
	for i := range d {
		d[i] = make([][]int, k+1)
		for j := range d[i] {
			d[i][j] = make([]int, len(vals))
		}
	}

	border := make([][]int, n)
	for i := range border {
		border[i] = make([]int, k+1)
	}

	sum := make([][]int, k+1)
	for i := range sum {
		sum[i] = make([]int, len(vals))
	}

	suf := make([][]int, n)
	for i := range suf {
		suf[i] = make([]int, k+1)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			pos := sort.SearchInts(vals, nums[i]-nums[j])
			for p := 1; p <= k; p++ {
				for border[j][p] < pos {
					sum[p][border[j][p]] = (sum[p][border[j][p]] - suf[j][p] + mod) % mod
					sum[p][border[j][p]] = (sum[p][border[j][p]] + d[j][p][border[j][p]]) % mod
					suf[j][p] = (suf[j][p] - d[j][p][border[j][p]] + mod) % mod
					border[j][p]++
					sum[p][border[j][p]] = (sum[p][border[j][p]] + suf[j][p]) % mod
				}
			}
		}

		d[i][1][len(vals)-1] = 1
		for p := 2; p <= k; p++ {
			for v := 0; v < len(vals); v++ {
				d[i][p][v] = sum[p-1][v]
			}
		}
		for p := 1; p <= k; p++ {
			for v := 0; v < len(vals); v++ {
				suf[i][p] = (suf[i][p] + d[i][p][v]) % mod
			}
			sum[p][0] = (sum[p][0] + suf[i][p]) % mod
		}
	}

	res := 0
	for i := 0; i < n; i++ {
		for v := 0; v < len(vals); v++ {
			res = (res + int(int64(vals[v])*int64(d[i][k][v])%mod)) % mod
		}
	}
	return res
}

func unique(arr []int) []int {
	if len(arr) == 0 {
		return arr
	}
	result := []int{arr[0]}
	for _, v := range arr {
		if v != result[len(result)-1] {
			result = append(result, v)
		}
	}
	return result
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return sumOfPowers(nums, k)
}
