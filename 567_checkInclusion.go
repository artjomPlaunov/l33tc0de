func checkInclusion(s1 string, s2 string) bool {
    s1Hash := make(map[rune]int)
    s2Hash := make(map[rune]int)
    for _, c := range s1 {
        s1Hash[c] += 1
    }
  
    windowStart := 0
    
    for windowEnd, c := range s2 {
        if s1Hash[c] == 0 {
            windowStart = windowEnd+1
            s2Hash = make(map[rune]int)
            continue
        }
        s2Hash[c] += 1
        for s2Hash[c] > s1Hash[c] {
            f := rune(s2[windowStart])
            s2Hash[f] -= 1
            windowStart += 1
        }
        if (windowEnd-windowStart+1) == len(s1) {
            return true
        }
    }
    
    return false
}
