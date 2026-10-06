package problem2286

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

type seg []struct{ l, r, min, sum int }

func (t seg) build(o, l, r int) {
	t[o].l, t[o].r = l, r
	if l == r {
		return
	}
	m := (l + r) >> 1
	t.build(o<<1, l, m)
	t.build(o<<1|1, m+1, r)
}

// Increase the element at index i by val
func (t seg) update(o, i, val int) {
	if t[o].l == t[o].r {
		t[o].min += val
		t[o].sum += val
		return
	}
	m := (t[o].l + t[o].r) >> 1
	if i <= m {
		t.update(o<<1, i, val)
	} else {
		t.update(o<<1|1, i, val)
	}
	lo, ro := t[o<<1], t[o<<1|1]
	t[o].min = min(lo.min, ro.min)
	t[o].sum = lo.sum + ro.sum
}

// Return the sum of elements in [l,r]
func (t seg) querySum(o, l, r int) (sum int) {
	if l <= t[o].l && t[o].r <= r {
		return t[o].sum
	}
	m := (t[o].l + t[o].r) >> 1
	if l <= m {
		sum = t.querySum(o<<1, l, r)
	}
	if r > m {
		sum += t.querySum(o<<1|1, l, r)
	}
	return
}

// Return the leftmost position in [0,r] whose value is <= val, or -1 if none exists
func (t seg) findFirst(o, r, val int) int {
	if t[o].min > val {
		return -1 // Every value in the interval exceeds val
	}
	if t[o].l == t[o].r {
		return t[o].l
	}
	m := (t[o].l + t[o].r) / 2
	if t[o*2].min <= val {
		return t.findFirst(o*2, r, val)
	}
	if r > m {
		return t.findFirst(o*2+1, r, val)
	}
	return -1
}

type BookMyShow struct {
	seg
	n, m int
}

func Constructor(n, m int) BookMyShow {
	t := make(seg, 2<<bits.Len(uint(n-1))) // Smaller than 4n
	t.build(1, 0, n-1)
	return BookMyShow{t, n, m}
}

func (t *BookMyShow) Gather(k, maxRow int) []int {
	// Find the first bucket that can hold k more liters of water
	r := t.findFirst(1, maxRow, t.m-k)
	if r < 0 { // No such bucket exists
		return nil
	}
	c := t.querySum(1, r, r)
	t.update(1, r, k) // Pour water
	return []int{r, c}
}

func (t *BookMyShow) Scatter(k, maxRow int) bool {
	// Total amount of water in [0,maxRow]
	s := t.querySum(1, 0, maxRow)
	if s > t.m*(maxRow+1)-k {
		return false // The buckets already contain too much water
	}
	// Start with the first bucket that is not full
	i := t.findFirst(1, maxRow, t.m-1)
	for k > 0 {
		left := min(t.m-t.querySum(1, i, i), k)
		t.update(1, i, left) // Pour water
		k -= left
		i++
	}
	return true
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * obj := Constructor(n, m);
 * param_1 := obj.Gather(k,maxRow);
 * param_2 := obj.Scatter(k,maxRow);
 */

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]any
	var ans []any
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	obj := Constructor(int(opValues[0][0].(float64)), int(opValues[0][1].(float64)))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "gather", "Gather":
			res = obj.Gather(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		case "scatter", "Scatter":
			res = obj.Scatter(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
