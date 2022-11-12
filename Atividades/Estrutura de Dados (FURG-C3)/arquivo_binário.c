#include <stdio.h>
#include <stdlib.h>

FILE *arq;

typedef struct{
    int codigo;
    char nome[30];
    int ativo;
}cliente;
cliente cli;

void cabeca(char t[20]){printf("======================== [%s] ========================\n",t);}

void inserir(){
    cabeca("Inserir");
    arq = fopen("arq3.dat", "ab");
    
    if (arq==NULL){printf("Erro");}
    else{
        fseek(arq,sizeof(cli)*0,SEEK_SET);
        
        printf("Digite o nome: ");
        scanf("%s", cli.nome);
        
        printf("Digite o codigo: ");
        scanf("%d", &cli.codigo);
        
        cli.ativo =1;
        
        fwrite(&cli, sizeof(cli), 1, arq);
    }
    fclose(arq);
    }
    
void listar(){
    cabeca("Lista");
    
    arq = fopen("arq3.dat", "a+b");
    
    fseek(arq,sizeof(cli)*0,SEEK_SET);
    fread(&cli, sizeof(cli), 1, arq);
    printf("\n");
    
    while (!feof(arq)){
       
       if(cli.ativo==1){
       printf("Codigo: %d\n", cli.codigo);
       printf("Nome: %s\n", cli.nome);
       printf("\n");
       }
       
       fread(&cli, sizeof(cli), 1, arq);
    }
    
    fclose(arq);
}

void remover(){
    int pos;
    arq = fopen("arq3.dat","r+b");
    if(arq==NULL){printf("Erro");}
    else{
        fseek(arq,sizeof(cli)*0,SEEK_SET);
        
        printf("Posição a ser removido: ");
        scanf("%d",&pos);
        
        fseek(arq,sizeof(cli)*(pos-1),SEEK_SET);
        
        cli.ativo = 0;
        
        fwrite(&cli.ativo,sizeof(cli),1,arq);
    }
    fclose(arq);
}

void alterar(){
    int psa;
    arq = fopen("arq3.dat","r+b");
    if(arq==NULL){printf("Erro");}
    else{
        printf("Posição a ser alterada: ");
        scanf("%d",&psa);
        
        fseek(arq,sizeof(cli)*(psa-1),SEEK_SET);
        
        printf("Digite o nome alterado: ");
        scanf("%s", cli.nome);
        
        printf("Digite o codigo alterado: ");
        scanf("%d", &cli.codigo);
        
        cli.ativo =1;
        fwrite(&cli, sizeof(cli), 1, arq);
        
        }
    fclose(arq);
}

int main(){
    int OP;
    cabeca("Menu");
    printf("(1)Inserir, (2)Listar, (3)Remover, (4)Alterar ou (5)Sair: ");
    scanf("%d", &OP);
    while(1){
        if (OP==1) inserir();
        if (OP==2) listar();
        if (OP==3) remover();
        if (OP==4) alterar();
        if (OP==5) break;
        cabeca("Menu");
        printf("(1)Inserir, (2)Listar, (3)Remover, (4)Alterar ou (5)Sair: ");
        scanf("%d", &OP);
    }
}