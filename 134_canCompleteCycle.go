func canCompleteCircuit(gas []int, cost []int) int {
    diff := make([]int, len(gas))
    sum := 0
    for i := 0; i < len(gas); i++ {
        diff[i] = gas[i] - cost[i]
        sum += diff[i]
    }
    if sum < 0 {
        return -1
    } else if len(gas) == 1 {
        return 0
    }
    i := 0
    for diff[i] < 0 {
        i += 1
    } 
    l := len(gas)
    start := i
    sum = diff[start] 
    
    for end := (i+1)%l; end != start; end = (end+1)%l {
        sum += diff[end]
        if sum < 0 {
            start = end
            for diff[start] < 0 {
                start = (start+1)%l
            }
            end = start
            sum = diff[start]
        }
    }
    return start
}
