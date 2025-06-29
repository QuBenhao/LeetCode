package problem2818

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

const MOD = 1000000007
const MaxN = 100001

var omega = make([]int, MaxN)

func init() {
	for i := 2; i < MaxN; i++ {
		if omega[i] == 0 {
			for j := i; j < MaxN; j += i {
				omega[j]++
			}
		}
	}
}

func fastPow(base, exp int64) int64 {
	result := int64(1)
	for exp > 0 {
		if exp%2 == 1 {
			result = (result * base) % MOD
		}
		base = (base * base) % MOD
		exp /= 2
	}
	return result
}

func maximumScore(nums []int, k int) int {
	n := len(nums)
	count := make([]int, n)
	idxes := make([]int, n)
	left := make([]int, n)
	right := make([]int, n)
	for i, num := range nums {
		count[i] = omega[num]
		idxes[i] = i
		left[i] = -1
		right[i] = n
	}
	var stack []int
	for i, cnt := range count {
		for len(stack) > 0 && count[stack[len(stack)-1]] < cnt {
			right[stack[len(stack)-1]] = i
			stack = stack[:len(stack)-1]
		}
		if len(stack) > 0 {
			left[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	sort.Slice(idxes, func(i, j int) bool { return nums[idxes[i]] > nums[idxes[j]] })
	ans := int64(1)
	for _, idx := range idxes {
		num := nums[idx]
		if num == 1 {
			break
		}
		l, r := left[idx], right[idx]
		take := min(int64(k), int64(r-idx)*int64(idx-l))
		ans = (ans * fastPow(int64(num), take)) % MOD
		k -= int(take)
		if k <= 0 {
			break
		}
	}
	return int(ans)
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

	return maximumScore(nums, k)
}
