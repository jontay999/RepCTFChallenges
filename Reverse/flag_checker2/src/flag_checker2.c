#include <stdio.h>
#include <string.h>


int encrypt(int c) {
    return (c + 1) ^ 37;
}

int main(){
    int encrypted_flag[] = {118, 99, 116, 89, 76, 85, 84, 67, 69, 95, 85, 83, 69, 93, 85, 86, 73, 67, 64, 69, 76, 71, 86, 64, 67, 86, 69, 66, 85, 86, 69, 80, 76, 79, 81, 69, 19, 64, 28, 22, 20, 16, 23, 17, 29, 67, 28, 28, 71, 67, 19, 18, 70, 23, 65, 28, 66, 29, 64, 71, 66, 31, 66, 23, 70, 29, 31, 70, 91};
    char guess[100];
    puts("Guess the flag part 2: ");
    fgets(guess, sizeof(guess), stdin);

    guess[strcspn(guess, "\n")] = 0;
    if(strlen(guess) != (sizeof(encrypted_flag) / sizeof(int))){
        puts("wrong length of flag!");
        return 1;
    }
    for (int i = 0; i < strlen(guess); i++) {
        char c = encrypt(guess[i]);
        if (c != encrypted_flag[i]){
            puts("Sorry, that's not correct.");
            return 1;
        }
    }
    puts("Congratulations! You've guessed the flag.");
    return 0;
}
