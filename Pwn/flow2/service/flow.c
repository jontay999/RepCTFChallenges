#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int chances(){
    return 40 + rand() % 6;
}

int main() {
    // Seed the RNG
    srand(time(NULL));
    int length = 10;
    char buffer[length];
    puts("Welcome to pwn 102! Maybe writing a `win()` function for you was too easy.\n");
    puts("Let's see you find a way to win by yourself.\n");
    int extra_chances = chances();
    printf("You'll get this amount of extra bytes: %d\n", extra_chances);
    setbuf(stdout,0);
    setbuf(stdin,0);
    fgets(buffer, length + extra_chances, stdin);
    return 0;
}
