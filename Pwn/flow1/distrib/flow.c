#include <stdio.h>
#include <stdlib.h>

void win(){
    printf("I'm in \n");
    FILE *file = fopen("flag.txt", "r");
    if (file) {
        char ch;
        while ((ch = fgetc(file)) != EOF) putchar(ch);
        fclose(file);
    }
	exit(0);
}

int main() {
    char buffer[30];
    printf("Welcome to pwn 101! I heard `gets` is unsafe so I used `fgets` instead!\n");
    setbuf(stdout,0);
    setbuf(stdin,0);
    fgets(buffer, 60, stdin);
    return 0;
}
