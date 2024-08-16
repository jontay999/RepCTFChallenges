// gcc -g -no-pie fmt1.c -o fmt1
#include <stdio.h>


int secret_code = 1;

int main() {
    char buffer[40];
    puts("I've learnt my lesson, no more buffer overflows for you...");
    puts("Instead, I'll just let you print some things out, surely that won't be bad right?");
    fgets(buffer, sizeof buffer, stdin);
    puts("Here's what you've printed:");
    printf(buffer);


    printf("Secret code is %i\n", secret_code);

    if(secret_code == 13) {
	puts("how did you do that??? Here's the flag for your troubles");
	FILE *file = fopen("flag.txt", "r");
        if (file) {
            char ch;
            while ((ch = fgetc(file)) != EOF) putchar(ch);
            fclose(file);
        }
    }
}
