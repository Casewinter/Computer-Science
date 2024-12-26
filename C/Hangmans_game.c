//Define max size for the words [x]
//Define max tries for the player [x]
//The word will be string literal, do not forget cast [x]

#include <stdio.h>
#include <string.h>

#define MAX_SIZE 256
#define MAX_TRIES 10

typedef struct
{
    char word[MAX_SIZE];
    char showing[MAX_SIZE];
    int tries;
    int word_len;
} Hangmans_game;

void starting_game(char *word, Hangmans_game *buffer){
    strcpy(buffer->showing, word);
    strcpy(buffer->word, word);

    int counter = 0;

    while(buffer->showing[counter] != '\0'){
        buffer->showing[counter] = '_';
        counter++;
    }

    buffer->word_len = counter;

};


void loop(Hangmans_game *game){
    
    int lifes_left = game->tries;
    char guess;
    int wrong_guess = 1;
    int chars_to_guess = game->word_len;
    char already_tried[MAX_SIZE];
    int counter = 0;

    while (lifes_left > 0)
    {
         printf("\n--------------x----------");
        printf("\nLetras ja tentadas:");
        for(int i = 0; i < counter; i++){
            printf("\n => %c", already_tried[i]);
        }
        printf("\n--------------x----------");
        printf("\nVidas %i ", lifes_left);
        printf("\n%s", game->showing);

        wrong_guess = 1;
        printf("\nTente uma letra: ");

        guess = getchar();
        getchar(); // Para consumir o '\n' da entrada anterior

        for(int index = 0; index < game->word_len; index++){
            if(game->word[index] == guess){
                chars_to_guess--;
                wrong_guess = 0;
                game->showing[index] = guess;
            }
        }
        if(wrong_guess) {
            lifes_left = lifes_left - 1;
            already_tried[counter] = guess;
            counter++;
        }


        if(chars_to_guess == 0){
            printf("\nParabens, voce acertou a palavra!!! -> %s", game->word);
            return;
        }
    }
    printf("\nVoce perdeu :c. A palavra era: %s", game->word);
}

int main(){

    Hangmans_game games_set= {"","",MAX_TRIES, 0};
    starting_game("teste", &games_set);
    loop(&games_set);
    
    return 0;
}