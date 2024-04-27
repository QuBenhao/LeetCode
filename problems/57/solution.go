func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func insert(intervals [][]int, newInterval []int) (ans [][]int) {
    left, right := newInterval[0], newInterval[1]
    for _, interval := range intervals {
        a, b := interval[0], interval[1]
        if b < left || a > right {
            if a > right {
                ans = append(ans, []int{left, right})
                left = 0x3f3f3f
                right = 0x3f3f3f
            }
            ans = append(ans, interval)
        } else {
            left = min(left, a)
            right = max(right, b)
        }
    }
    if left != 0x3f3f3f && (len(ans) == 0 || ans[len(ans) - 1][1] < left) {
        ans = append(ans, []int{left, right})
    }
    return
}