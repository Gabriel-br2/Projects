#include <stdio.h>
#include <stdlib.h>

int* uniao(int *x1, int *x2, int n1, int n2, int qtd){
  int *x3, i=0, j=0, ax=0;
  int q = n1+n2;
  x3=calloc(q,sizeof(int*));
  
  for(int d = 0; d <n1; d++){
    x3[d] = x1[d];
    ax = d;
  }

  for(int e = 0; e<n2; e++){
    x3[e+ax+1] = x2[e];
  }


  for(int f = 0; f<q;f++){
    printf("%d ",x3[f]);
  }

  return 0;
}

int main() {
  int *x1,*x2;
  int tam1,tam2,qtd;
     
  printf("Tamanho de x1: ");
  scanf("%d",&tam1);

  printf("Tamanho de x2: ");
  scanf("%d",&tam2);

  x1=calloc(tam1,sizeof(int*));
  x2=calloc(tam2,sizeof(int*));
  
  for(int a=0; a<tam1;a++){
    printf("valor de x1[%d]: ",a);
    scanf("%d",&x1[a]);
  } 
  
  for(int b=0; b<tam2;b++){
    printf("valor de x2[%d]: ",b);
    scanf("%d",&x2[b]);
  }

  uniao(x1,x2,tam1,tam2,qtd);

  return 0;
}
  