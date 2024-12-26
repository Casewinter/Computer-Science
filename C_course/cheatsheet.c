#include <stdio.h>
#include <stdbool.h>


char a = 'c';                                   //Single character      %c 
char b[] = "Bro";                               //array of characters   %s
char f = 100;                                   //1 byte (-128 to 127) interger %d or %c
                                                //If you printf as a character, C will use ASCII Table to convert. 
                                                //100 is d

unsigned char g = 255;                          //1 byte, but without negative part (0 to 255) %d or %c

float c = 3.1459265358793;                      //4 bytes (32 bit of precision) 6 - 7 digits %f
double d = 3.1459265358793;                     //8 bytes (64 bits of precision) 15 - 16 digits %1f
                                                //%.2f to print just 2 digits after dot

bool e = true;                                  //1 bytes (true or false) %d where 1 is true and 0 false

short int h = 32767;                            //2 bytes (-32,768 to 32,767) %d
unsigned short int i = 65535;                   //2 bytes (0 to 65,535) %d

int j =  1111111;                               //4 bytes (-2,147,483,648  to -2,147,483,647) %d
unsigned int l = 1111111;                       //4 bytes (0 to 4,294,967,295) %u

long long int k = 1;                            //8 bytes (-9 quintillion to 9 quintillion) %lld
unsigned long long int m = 1U;                  //8 bytes (0 to 18 quintillion) %llu
                                                //U is necessary to avoid warnings

//%1 = minimum field with
//%- left aling 
//\n break line
//\t tab

const char aa[] = "hi";                          //like in JS


//  arithmetic operators
//  + - * / %(modulus) ++ -- all are like in JS

//  augmented assingment operators
//  += -=                    also, like in JS

//  User input
//  int age;
//  char name[25];
//  scanf("%d", &age); 
//  scanf do no catchs white spaces for this, we need to use
//  fgets(name, 25, stdin);
//  when we run this, \n will be include in side of our array. 
//  char c;
//  c = getchar();


#include <math.h>

int main(){

    double a = sqrt(9);                                  //square root
    int b = pow(2, 4);                                   //power of => 4^2
    int c = round(3.14);                                 //round
    int d = ceil(3.14);                                  //round always to up
    int e = floor(3.14);                                 //round always to down    
    int f = fabs(-100);                                  //absolute value
    int g = log(3);
    double h = sin(45);  
    double i = cos(45);
    double j = tan(45);                                 

    return 0;
};
