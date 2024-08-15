// gcc -g -no-pie -fno-stack-protector -Wl,-z,norelro -z execstack flow2.c -o flow2
#include <stdio.h>

void enter_flow_state() {
    char buffer[300];
    printf("address: %p\n", (void *)buffer); 
    puts("Maybe giving you a `win()` function was too easy...");
    gets(buffer);
}

void main() {
    enter_flow_state();
}
