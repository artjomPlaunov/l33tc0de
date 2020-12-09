func numPairsDivisibleBy60(time []int) int {
    hash := make(map[int]int)
    res := 0
    for _, v := range time {
        mod := v % 60
        if mod == 0 {
            res += hash[mod]
            hash[mod] += 1
        } else {
            res += hash[60-mod]
            hash[mod] += 1
        }
    }
    return res
}
