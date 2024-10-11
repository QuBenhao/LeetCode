package problem3164

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfPairs(nums1, nums2 []int, k int) (ans int64) {
    cnt1 := map[int]int{}
    u := 0
    for _, x := range nums1 {
        if x%k == 0 {
            u = max(u, x/k)
            cnt1[x/k]++
        }
    }
    if u == 0 {
        return
    }

    cnt2 := map[int]int{}
    for _, x := range nums2 {
        cnt2[x]++
    }

    for x, cnt := range cnt2 {
        s := 0
        for y := x; y <= u; y += x { // 枚举 x 的倍数
            s += cnt1[y]
        }
        ans += int64(s * cnt)
    }
    return
}


func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums1 []int
	var nums2 []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return numberOfPairs(nums1, nums2, k)
}
