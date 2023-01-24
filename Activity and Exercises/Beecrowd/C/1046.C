#include <stdio.h>
 
int main() {
  int hi = 0;int hf = 0; int total = 0;
  scanf("%d %d",&hi,&hf);
  if (hi == hf){
      total = 24;  	
  }
  else if (hi < hf){
    total = hf-hi;  	
  }
  else if (hi > hf){
    total = hf - (hi-24);  	
  }
  printf("O JOGO DUROU %d HORA(S)\n",total);
  return 0;
}