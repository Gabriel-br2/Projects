#include <stdio.h>
#include <string.h>

int main() {
  char t1[13];
  char t2[13];
  char t3[13];

  scanf("%12s", t1);
  scanf("%12s", t2);
  scanf("%12s", t3);

if(strcmp(t1,"vertebrado")==0){
    if(strcmp(t2,"ave")==0){
      if(strcmp(t3,"carnivoro")==0){
        printf("aguia\n");        
      }
      if(strcmp(t3,"onivoro")==0){
        printf("pomba\n");
      }
    }
    if(strcmp(t2,"mamifero")==0){
      if(strcmp(t3,"onivoro")==0){
        printf("homem\n");
      }
      if(strcmp(t3,"herbivoro")==0){
        printf("vaca\n");
      }
    }
  }
  if(strcmp(t1,"invertebrado")==0){
    if(strcmp(t2,"inseto")==0){
      if(strcmp(t3,"hematofago")==0){
        printf("pulga\n");
      }
      if(strcmp(t3,"herbivoro")==0){
        printf("lagarta\n");
      }
    }
    if(strcmp(t2,"anelideo")==0){
      if(strcmp(t3,"hematofago")==0){
        printf("sanguessuga\n");
      }
      if(strcmp(t3,"onivoro")==0){
        printf("minhoca\n");
      }   
    }
  }
  return 0;
}