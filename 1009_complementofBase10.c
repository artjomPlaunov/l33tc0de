int bitwiseComplement(int N){
    if (N == 0) {
        return 1;
    } else if (N == 1) {
        return 0;
    }
    
    int flag = 1;
    int pow = 0;
    int res = 0;
    
    while (N) {
        int q = N % 2;
        if (!q) {
            res += 1 << pow;
        }
        N /= 2;
        pow += 1;
    }
    return res;
}
