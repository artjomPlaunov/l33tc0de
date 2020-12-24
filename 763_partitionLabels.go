type Range struct {
    lo,hi int
}

func partitionLabels(S string) []int {
    
    res := make([]int, 0)
    if len(S) == 0 {
        return res
    }
    
    hash := make(map[rune]*Range)
    for i, c := range S {
        if val, ok := hash[c]; ok {
            val.hi = i
        } else {
            r := &Range{i,i}
            hash[c] = r
        }
    }
    
    start := 0
    for start < len(S) {
        end := hash[rune(S[start])].hi
        for i := start+1; i < end; i++ {
            c := rune(S[i])
            if hash[c].hi > end {
                end = hash[c].hi
            }
        }
        res = append(res, end-start+1)
        start = end+1
    }
    return res
}
