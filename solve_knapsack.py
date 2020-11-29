def solve_knapsack(profits, weights, capacity):
    '''
    # Brute Force Solution
    return helper(profits, weights, capacity, 0)
    '''

    '''
    # Top-Down Memoized Solution
    memo = {}
    DP(profits, weights, capacity, 0, memo)
    return memo[(0,capacity)]
    '''

    # Bottom-Up Solution O(N*C) Space/Complexity
    '''
    memo = [[0]*(capacity+1) for _ in range(len(profits))]
   
    for i in range(1,capacity+1):
        if weights[0] <= i:
            memo[0][i] = profits[0]

    for i in range(1,len(profits)):
        for c in range(1, capacity+1):
            include = 0
            dontInclude = 0
            if c-weights[i] >= 0:
                include = profits[i] + memo[i-1][c-weights[i]]
            dontInclude = memo[i-1][c]
            memo[i][c] = max(include,dontInclude)
   
    return memo[len(profits)-1][c]
    '''

    # Bottom-up O(C) Space and O(N*C) time
    memo = [[0]*(capacity+1) for _ in range(2)]
    for c in range(1, capacity+1):
        if weights[0] <= c:
            memo[0][c] = profits[0]

    for i in range(1, len(profits)):
        for c in range(1, capacity+1):
            include, dontInclude = 0,0
            if c-weights[i] >= 0:
                include = profits[i] + memo[(i-1)%2][c-weights[i]]
            dontInclude = memo[(i-1)%2][c]
            memo[i%2][c] = max(include,dontInclude)
    return memo[(len(profits)-1)%2][capacity]

def DP(profits, weights, capacity, i, memo):
    if i >= len(profits) or capacity <= 0:
        memo[(i,capacity)] = 0
    if (i, capacity) in memo:
        return
    lProfit = 0
    if weights[i] <= capacity:
        DP(profits, weights, capacity-weights[i], i+1, memo)
        lProfit =   profits[i] + memo[(i+1, capacity-weights[i])]

    DP(profits, weights, capacity, i+1, memo)
    memo[(i, capacity)] = max(lProfit, memo[(i+1,capacity)])

def helper(profits, weights, capacity, index):
    if index >= len(profits) or capacity <= 0:
        return 0
    lProfit = 0
    if weights[index] <= capacity:
        lProfit =   (profits[index] + 
                    helper(profits, weights, capacity-weights[index], index+1))
    rProfit = helper(profits, weights, capacity, index+1)

    return max(lProfit, rProfit)

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
