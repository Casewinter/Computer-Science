// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//alias da estrututa
typedef struct  {
    char *data;
    size_t size;
    size_t capacity;
} DynamicBuffer ;

//Inicializando o buffer
void initializeBuffer(DynamicBuffer *buffer, size_t initialCapacity){
    buffer->data = malloc(initialCapacity *sizeof(char));
    if(buffer->data == NULL){
        fprintf(stderr, "Erro ao alocar memória para o buffer. \n");
        exit(1); //Encerra o programa em caso de erro de alocação
    }
    buffer->size = 0;   //Coloca o local index do array no ponto correto, começando em 0
    buffer->capacity = initialCapacity; //Define a alocação inicial
}

//Liberação da memória
void destroyBuffer(DynamicBuffer *buffer) {
    free(buffer->data);  // Libera a memória do buffer
    buffer->data = NULL; // Evita dangling pointers
    buffer->size = 0;    // Reseta tamanho
    buffer->capacity = 0;// Reseta capacidade
}

void resizeMemory(DynamicBuffer *buffer, size_t newCapacity){
    buffer->capacity += sizeof(char) * newCapacity;
    buffer->data = realloc(buffer->data, buffer->capacity);
       
    if(!buffer->data){
        fprintf(stderr, "Erro ao redimencionar a memória para o buffer. \n");
        exit(1); //Encerra o programa em caso de erro de alocação
    }
}

//Atuliazando o buffer com mais texto
void readInput(DynamicBuffer *buffer){
    char ch;
    
    printf("Digite seu texto (pressione Enter para encerrar)\n");
    
    while((ch = getchar()) != '\n') {
          
           if(buffer->size + 1 >= buffer->capacity){
           
            // Se o espaço restante no buffer for insuficiente, redimensionar
            // Aumenta a capacidade em 256
            resizeMemory(buffer, 256);
            /*Neste momento, size está no final do texto, não do buffer. Queremos acessar esse 
            index e fazer o append. Após isso, podemos atualizar o size e mover o index para o 
            final do texto */
        }  
            buffer->data[buffer->size] = ch;
            buffer->size++;
    }
    buffer->data[buffer->size] = '\0';
}

int main() {
    //Cria a estrutura
    DynamicBuffer buffer;

    //Inicia o buffer com a capacidade inicial de 16 de carateres
    initializeBuffer(&buffer, 16);
    
    printf("Buffer inicializado! \n");
    printf("Capacidade: %zu\n", buffer.capacity);
    printf("Tamanho atual: %zu\n", buffer.size);
    printf("Texto armazenado: %s\n", buffer.data);
    printf(" \n");
    
     // Lê a entrada do usuário
    readInput(&buffer);
    printf("  \n");
    printf("Capacidade: %zu\n", buffer.capacity);
    printf("Tamanho atual: %zu\n", buffer.size);
    printf("Texto armazenado: %s\n", buffer.data);


     //Liberando a memória no final da execução
    destroyBuffer(&buffer);

    return 0;
}