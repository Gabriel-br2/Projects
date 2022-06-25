#include <stdio.h>
#include <math.h>
 
int main() {
  float x1 = 0; float x2 = 0;
  float y1 = 0; float y2 = 0; 
  scanf("%f %f", &x1, &y1);
  scanf("%f %f", &x2, &y2); 
  float a = pow((pow(x2-x1,2) + pow(y2-y1,2)),0.5);
  printf("%.4f\n", a);
  return 0;
}