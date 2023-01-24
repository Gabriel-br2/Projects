#include <stdio.h>

int contar(int vet[100]){
    for(int a =0;a<100;a++){
      if(vet[a] ==0){
        return a;
      }
    }
  return 0;
}

int main() {
  int N;
  scanf("%d",&N);
  
  int ced[100] = {100,50,20,10,5,2,1,0};
  int len_ced = contar(ced);
  
  printf("%d\n",N);
  
  for(int a = 0; a<len_ced;a++){
    printf("%d nota(s) de R$ %d,00\n",N/ced[a],ced[a]);
    N = N % ced[a];
    
  } 
    return 0;
}