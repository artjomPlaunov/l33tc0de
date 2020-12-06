func findSubstring(s string, words []string) []int {
    res := make([]int,0)
    for offset := 0; offset < len(words[0]); offset += 1 {
        res = aux(s[offset:], words, res, offset)
    }
    return res
}


func aux(s string, words []string, res []int, offset int) []int {

    if len(words) == 0 {
        return res
    }
    wordLen := len(words[0])
    wordMap := make(map[string]int)
    stringMap := make(map[string]int)
    count := 0
    for _, word := range words {
        wordMap[word] += 1
    }
    windowStart := 0
    for windowEnd := 0; windowEnd < len(s); windowEnd += wordLen {
        if (windowEnd + wordLen) >= len(s) + 1 {
            return res
        }
        curWord := s[windowEnd:windowEnd+wordLen]
        if wordMap[curWord] == 0 {
            windowStart = windowEnd + wordLen
            stringMap = make(map[string]int)
            count = 0 
            continue
        }
        
        stringMap[curWord] += 1
        count += 1
        
        for stringMap[curWord] > wordMap[curWord] {
            startWord := s[windowStart:windowStart+wordLen]
            windowStart += wordLen
            stringMap[startWord] -= 1
            count -= 1
        }
        
        if count == len(words) {
            res = append(res, windowStart+offset)
        }
    }
    return res
}
