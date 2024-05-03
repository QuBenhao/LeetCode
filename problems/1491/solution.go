func average(salary []int) float64 {
    mn, mx, sm := 0x3f3f3f, 0, 0
    for _, v := range salary {
        if v > mx {
            mx = v
        }
        if v < mn {
            mn = v
        }
        sm += v
    }
    return float64(sm - mx - mn) / float64(len(salary) - 2)
}