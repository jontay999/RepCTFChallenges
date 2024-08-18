// gcc -g -no-pie -fstack-protector -z noexecstack -o real real.c

#include <stdio.h>
#include <stdlib.h>

void hint(){
  puts("Since I'm nice, I'll give you a hint, but first let me fill up the hints");
  void *is_this_really_a_hint = (void *)fgets;
  unsigned long long hint_buffer[10];
  int index;
  for(int i = 0; i < 10; i++){
    hint_buffer[i] = i*10;
  }
 
  printf("Enter an integer: ");
  if (scanf("%d", &index) != 1) {
    puts("Invalid input.");
    exit(1);
  }
  if (index >= 10){
    puts("Index out of bounds! No cheating!");
    exit(1);
  }

  printf("Here's a hint: hint_buffer[%d] = %p\n", index, hint_buffer[index]);
}

void fmt2(){
  setbuf(stdin,0);
  setbuf(stdout,0);
  char buffer[100];
  puts("no more buffer overflows...");
  fgets(buffer, sizeof(buffer), stdin);
  puts("But, I'll let you confirm what you've written");

  printf(buffer);
  puts("Did you see that? Maybe once more for you");
  printf(buffer);
  puts("Hope you had fun learning about format strings :)");
}

int main(){
  hint();
  fmt2();
}
