#include <stdio.h>

int main(){
    const double pi = 3.14159;

    double radius;
    double circumference;
    double area;


    printf("Enter radius of a circle: \t");
    scanf("%lf", &radius);

    circumference = 2 * pi * radius;
    area = pi * radius * radius;

    printf("\n Circumference: %lf", circumference);
    printf("\n Area:  %lf", area);

    return 0;
}