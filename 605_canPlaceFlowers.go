func canPlaceFlowers(flowerbed []int, n int) bool {
    count := 0
    i := 0
    for i < len(flowerbed) {
        cur := 0
        if i == 0 {
            if flowerbed[i] == 0 {
                cur, i = placeFlowers(flowerbed, i, true)
            } else {
                cur, i = 0, i+1
            }
        } else {
            if flowerbed[i] == 0 {
                cur, i = placeFlowers(flowerbed, i, false)
            } else {
                cur, i = 0, i+1
            }
        }
        count += cur
    }
    if count >= n {
        return true
    } else {
        return false
    }
}

func placeFlowers(f []int, i int, edge bool) (int,int) {
    res := 0
    if !edge {
        i = i+1
    }
    for i < len(f) && f[i] != 1 {
        if (i+1) == len(f) {
            return res+1, i+1
        } else {
            if f[i+1] == 1 {
                return res, i+1
            } else {
                res,i = res+1, i+2
            }
        }
    }
    return res, i
}
