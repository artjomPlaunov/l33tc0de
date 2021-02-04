int hammingWeight(uint32_t n) {
    uint32_t mask = 1;
    uint32_t res = 0;
    while (n) {
        res += (mask&n);
        n >>= 1;
    }
    return res;
}
