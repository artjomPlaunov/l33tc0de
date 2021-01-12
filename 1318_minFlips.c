int minFlips(int a, int b, int c){
    int res = 0;
    for (int i = 0; i < 32; i++) {
        int _a = (a>>i)&1;
        int _b = (b>>i)&1;
        int _c = (c>>i)&1;
        if (_c) {
            if (!_a && !_b) {
                res += 1;
            }
        } else {
            if (_a && _b) { 
                res += 2;
            } else if (_a || _b) {
                res += 1;
            }
        }
    }
    return res;
}
