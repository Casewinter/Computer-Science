#include <stdio.h>
#include <math.h>

int main(){

    double a;
    double b;
    double c;

    printf("Enter side of A: \n");
    scanf("%lf", &a);

    printf("Enter side of B: \n");
    scanf("%lf", &b);

    c = sqrt(a * a + b * b);

    printf("Hypotenuse is =>  %lf\n", c);

    return 0;
}