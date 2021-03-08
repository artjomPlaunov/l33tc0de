func distributeCandies(candyType []int) int {
    hash := make(map[int]bool)
    for _,v := range candyType {
        hash[v] = true
    }
    count := len(hash)
    if count > len(candyType)/2 {
        return len(candyType)/2
    } else {
        return count
    }
}
