#include <stdio.h>
#include <string.h>

int main(){
    const char flag[] = "REP{have_you_heard_of_decompilers}"; 
    char guess[50];
    puts("Guess the flag: ");
    fgets(guess, sizeof(guess), stdin);

    // remove the trailing new line chracter
    guess[strcspn(guess, "\n")] = 0;

    // Compare the guessed password with the predefined password
    if (strcmp(guess, flag) == 0) {
        puts("Congratulations! You've guessed the flag.");
    } else {
        puts("Sorry, that's not correct. Try again.");
    }

    return 0;
}
