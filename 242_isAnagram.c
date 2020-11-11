bool isAnagram(char * s, char * t){
    int hash[26]; 
    for (int i = 0; i < 26; i++) 
        hash[i] = 0;
    for (char * c = s; *c != '\0'; c++){
        hash[(*c)-97]++;
    }
    
    int secondHash[26];
    for (int i = 0; i < 26; i++) 
        secondHash[i] = 0;
    for (char *c = t; *c != '\0'; c++)
        secondHash[(*c)-97]++;

    for (int i=0; i < 26; i++) 
        if (hash[i] != secondHash[i])
            return false;
        
    return true;
}
