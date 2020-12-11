func validMountainArray(arr []int) bool {
    if len(arr) < 3 {
        return false
    }
    if arr[1] <= arr[0] {
        return false
    }
    inc := true
    for i := 0; i < len(arr)-1; i++ {
        if inc {
            if arr[i] == arr[i+1] {
                return false
            } else if arr[i] < arr[i+1] {
                continue
            } else {
                inc = false
            }
        } else {
            if arr[i] == arr[i+1] {
                return false
            } else if arr[i] > arr[i+1] {
                continue
            } else {
                return false
            }
        }
    }
    if inc == true {
        return false
    }
    return true
}
