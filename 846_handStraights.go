func isNStraightHand(hand []int, W int) bool {
    sort.Ints(hand)
    
    if len(hand)%W != 0 {
        return false
    }
    
    counts := make(map[int]int)
    for _, v := range hand {
        counts[v] += 1
    }
    
    for _, v := range(hand) {
        if counts[v] == 0 {
            continue
        }
        group := 1
        counts[v] -= 1
        for group < W {
            if counts[v+1] > 0 {
                group += 1
                counts[v+1] -= 1
                v += 1
            } else {
                return false
            }
        }
    }
    
    return true
}

/*
1, 2, 2, 3, 3, 4, 6, 7, 8

1 : 0
2 : 0
3: 0
4: 0
6: 1
7: 1
8: 1

1, 2, 3




*/
