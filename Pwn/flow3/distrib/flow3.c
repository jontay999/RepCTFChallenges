#include <stdio.h>
#include <stdlib.h>

void flow() {
    char buffer[40];
    puts("Flowing flowing");
    gets(buffer);
}

int main() {
    setbuf(stdout,0);
    setbuf(stdin,0);
    puts("Welcome to pwn103, now with NX enabled");
    flow();
}

void flag(int check, int check2) {
    if(check == 0xdeadc0de && check2 == 1337) {
        puts("I'm in 😎😎😎...");
        FILE *file = fopen("flag.txt", "r");
        if (file) {
            char ch;
            while ((ch = fgetc(file)) != EOF) putchar(ch);
            fclose(file);
        }
        exit(0);
    }
}
