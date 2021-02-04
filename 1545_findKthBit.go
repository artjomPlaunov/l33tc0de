import "strconv"
import "math"

func findKthBit(n int, k int) byte {
    num := strconv.Itoa(aux(n,k))
    return byte(num[0])
}

func aux(n int, k int) int {
    if n == 1 {
        return 0
    } 
    sLen := math.Pow(2, float64(n)) - 1
    sHalf := math.Ceil(sLen/2.0)
    if sHalf == float64(k) {
        return 1
    }

    if k < int(sHalf) {
        return aux(n-1, k)
    }
    
    newK := k-int(sHalf)
    newK = int(sHalf)-newK
    return 1 ^ aux(n-1,newK)
}
