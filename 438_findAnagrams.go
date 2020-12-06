func findAnagrams(s string, p string) []int {
    // Result list
    res := make([]int,0)
    
    pHash := make(map[rune]int)
    for _, c := range p {
        pHash[c] += 1
    }
    sHash := make(map[rune]int)
    windowStart := 0
    
    for windowEnd, c := range s {
        if pHash[c] == 0 {
            windowStart = windowEnd+1
            sHash = make(map[rune]int)
            continue
        }
        sHash[c] += 1
        for sHash[c] > pHash[c] {
            front := rune(s[windowStart])
            sHash[front] -= 1
            windowStart += 1
        }
        if (windowEnd-windowStart+1) == len(p) {
            res = append(res, windowStart)
            front := rune(s[windowStart])
            sHash[front] -= 1
            windowStart += 1
        }
    }
    return res
}
