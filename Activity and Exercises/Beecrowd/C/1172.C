#include <stdio.h>

int main() {
  for(int a=0;a < 10;a++){
    int x = 0;
    scanf("%d",&x);
    if(x<=0){
      x = 1;
    }
    printf("X[%d] = %d\n",a,x);
  }
    return 0;
}
