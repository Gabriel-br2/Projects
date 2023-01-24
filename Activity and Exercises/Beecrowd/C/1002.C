#include <stdio.h>

int main(){
    double Raio,Area;
    
    scanf("%lf", &Raio);
    Area = 3.14159*Raio*Raio;
    printf("A=%1.4lf\n",Area);
    
    return 0;
}