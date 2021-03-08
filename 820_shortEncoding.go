type TrieNode struct {
    Next map[byte]*TrieNode
}

func (t TrieNode) Add(word []byte) {
    if len(word) == 0 {
        return 
    }
    if _,ok := t.Next[word[0]]; ok {
        t.Next[word[0]].Add(word[1:])
    } else {
        t.Next[word[0]] = &TrieNode{make(map[byte]*TrieNode)}
        t.Next[word[0]].Add(word[1:])
    }
}

func (t TrieNode) getDepths(depth int) int {
    
    if len(t.Next) == 0 {
        return depth+1
    }
    
    res := 0
    for _,v := range t.Next {
        res += v.getDepths(depth+1)
    }
    return res
}

func minimumLengthEncoding(words []string) int {
    root := &TrieNode{make(map[byte]*TrieNode)}
    for _, word := range words {
        rev := make([]byte, 0)
        for i := len(word)-1; i >= 0; i-- {
            rev = append(rev, word[i])
        }
        root.Add(rev)
    }
    
    return root.getDepths(0)
}
