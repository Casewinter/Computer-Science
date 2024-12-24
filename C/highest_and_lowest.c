#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *strnum = "8 3 -5 42 -1 0 0 -9 4 7 4 -4";

int main() {
    char *strnumArray = malloc(strlen(strnum) + 1);
    strcpy(strnumArray, strnum);
    int capacity = 10, count = 0;
    int *numbers = malloc(sizeof(int) * capacity);
    
    
    if(numbers == NULL){
        fprintf(stderr, "Fatal error \n");
        exit(1);
    };
    char *token = strtok(strnumArray, " ");
    while(token != NULL){
        if(count >= capacity){
            capacity *= 2;
            numbers = realloc(numbers, sizeof(int) * capacity);
        }
         if(numbers == NULL){
            fprintf(stderr, "Fatal error \n");
            exit(1);
        };
        numbers[count++] = atoi(token);
        token = strtok(NULL, " ");
    }

    int highest = numbers[0], lower = numbers[0];
    for(int i = 0; i < count; i++){
         if(highest < numbers[i] ){
             highest = numbers[i];
         }
         if(lower >  numbers[i] ){
             lower = numbers[i];
         }
    }
    free(numbers);
    printf("%d %d", highest, lower);
    return 0;
}