type Node struct {
    Next, Prev * Node
    Key, Val int
}

type List struct {
    Head, Tail * Node
}

// Splice a node from the list and set prev/next pointers to nil
func (this *List) Splice(node * Node) {
    if node == this.Tail {
        this.Pop()
    } else if node == this.Head {
        this.Head = node.Next
        this.Head.Prev = nil
        node.Next = nil
    } else {
        node.Prev.Next = node.Next
        node.Next.Prev = node.Prev
        node.Prev = nil
        node.Next = nil
    }
}

// Push element to front of the list
func (this *List) Push(newHead * Node) {
    
    // If the list is empty
    if this.Head == nil {
        this.Head = newHead
        this.Tail = newHead
    // If the list has one element
    } else {
        tmp := this.Head
        this.Head = newHead
        newHead.Next = tmp
        tmp.Prev = newHead
    }
}

// Pop element pointed to by tail
// Precond: List is non-empty
func (this *List) Pop() {
    // If List is a single element
    if this.Head == this.Tail {
        this.Head = nil
        this.Tail = nil
    } else {
        newTail := this.Tail.Prev
        newTail.Next = nil
        this.Tail = newTail
    }
}

type LRUCache struct {
    Len, Cap int
    Hash map[int]*Node
    LRUList List
}

func Constructor(capacity int) LRUCache {
    return LRUCache {                                                           
        Len: 0,                                                                 
        Cap: capacity,                                                          
        Hash: map[int]*Node{},                                                  
        LRUList:  List{nil,nil},                                                    
    }    
}

func (this *LRUCache) Get(key int) int {
    if _, ok := this.Hash[key]; !ok {
        return -1
    } else {
        nodePtr := this.Hash[key]
        this.LRUList.Splice(nodePtr)
        this.LRUList.Push(nodePtr)
        return nodePtr.Val
    }
}

func (this *LRUCache) Put(key int, value int)  {
    // If key does not exist yet
    if _, ok := this.Hash[key]; !ok { 
        // If LRU cache is full then evict an element to insert new key
        if (this.Len == this.Cap) { 
            // Clear hash table key 
            evictKey := this.LRUList.Tail.Key
            delete(this.Hash, evictKey)
            // Pop element from LRU List
            this.LRUList.Pop()
        } 
        // Push element to the front of the cache
        newHead := Node{Next: nil, Prev: nil, Key: key, Val: value,}
        this.LRUList.Push(&newHead)
        this.Hash[key] = this.LRUList.Head
        if this.Len < this.Cap {
            this.Len += 1
        }
    // Key already exists
    } else {
        if this.LRUList.Head.Key == key {
            this.LRUList.Head.Val = value
        } else {
            nodePtr := this.Hash[key]
            nodePtr.Val = value
            this.LRUList.Splice(nodePtr)
            this.LRUList.Push(nodePtr)
        }
    }

}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
