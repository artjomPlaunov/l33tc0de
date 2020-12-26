import "math"

func reverse(b []byte) []byte {
    for i,j := 0, len(b)-1; i < j; i,j = i+1, j-1 {
        b[i],b[j] = b[j],b[i]
    }
    return b
}

func decodeString(s string) string {
    stack := make([]byte,0)
    for i,_ := range s {
        ch := s[i]
        if ch == ']' {
            cur := make([]byte,0)
            for stack[len(stack)-1] != '[' {
                cur = append(cur,stack[len(stack)-1])
                stack = stack[:len(stack)-1]
            }
            stack = stack[:len(stack)-1]
            cur = reverse(cur)
            n, pow := 0,0
            for (len(stack) > 0 && (stack[len(stack)-1] >= 48) && stack[len(stack)-1] <= 57) {
                digit := int(stack[len(stack)-1] - 48)
                n += digit * int(math.Pow10(pow))
                pow += 1
                stack = stack[:len(stack)-1]
            }
            for n > 0 {
                stack = append(stack, cur...)
                n -= 1
            }
            
        } else {
            stack = append(stack, ch)
        }
    }
    return string(stack)
}
