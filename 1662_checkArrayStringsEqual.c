

bool arrayStringsAreEqual(char ** word1, int word1Size, char ** word2, int word2Size){
    int outer_i = 0;
    int outer_j = 0;
    
    char *i = word1[outer_i];
    char *j = word2[outer_j];
    
    while (outer_i < word1Size && outer_j < word2Size) {
        if (*i != *j) {
            return false;
        } 
        i++;
        j++;
        if (*i == '\0') {
            outer_i += 1;
            if (outer_i < word1Size) {
                i = word1[outer_i];
            }
        }
        if (*j == '\0') {
            outer_j += 1;
            if (outer_j < word2Size) {
                j = word2[outer_j];
            }
        }
    }
    
    if (outer_i < word1Size || outer_j < word2Size) {
        return false;
    } else {
        return true;
    }
}
