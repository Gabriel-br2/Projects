#include <stdio.h>
#include <stdlib.h>

void matriz_unidimensional(){
    int *vetor, tamanho;
    
    printf("Quantos valores deseja inserir: ");
    scanf("%d",&tamanho);

    vetor = calloc(tamanho,sizeof(int));
    
    for(int a = 0; a<tamanho;a++){
        printf("matriz[%d]: ",a);
        scanf("%d",&vetor[a]);
    }
    
    for(int b = 0; b<tamanho;b++){
        printf("%d ",vetor[b]);
    }
    
    free(vetor);
}

void matriz_bidimensional(){
    int **matriz, tamanho;

    printf("Quantos valores deseja inserir: ");
    scanf("%d",&tamanho);

    matriz = calloc(tamanho,sizeof(int));
    
    for(int a = 0;a<tamanho;a++){
        matriz[a] = calloc(tamanho,sizeof(int));
        for (int b = 0; b<tamanho;b++){
            printf("Matriz[%d][%d]: ",a,b);
            scanf("%d",&matriz[a][b]);
        }
    }  
    for(int c = 0; c < tamanho;c++){
        for(int d = 0; d < tamanho;d++){
            printf(" %d ",matriz[c][d]);
        }
        printf("\n");
        free(matriz[c]);
    }
    free(matriz);
}

void matriz_tridimensional(){
    int ***matriz, tamanho;

    printf("Quantos valores deseja inserir: ");
    scanf("%d",&tamanho);
    
    matriz = calloc(tamanho,sizeof(int));

    for(int a = 0; a < tamanho; a++){
        matriz[a] = calloc(tamanho,sizeof(int));
        
        for(int b = 0;b < tamanho ;b++){
            matriz[a][b] = calloc(tamanho,sizeof(int));
            
            for(int c = 0; c < tamanho; c++){
                printf("Matriz[%d][%d][%d]: ",a,b,c);
                scanf("%d",&matriz[a][b][c]); 
            }
        }
    }
    for(int d = 0; d < tamanho;d++){
        for(int e = 0; e < tamanho;e++){    
            for(int f = 0; f < tamanho;f++){
                printf(" %d ",matriz[d][e][f]);
            }
            printf("\n");
            free(matriz[d][e]);
        }
        printf("\n -------------------------- \n");
        free(matriz[d]);
    }
    free(matriz);
}


int main(){
    int m;
    printf("Inserir matriz de 1, 2 ou 3 dimensões: ");
    scanf("%d", &m);
    if(m == 1){
        matriz_unidimensional();
    }
    else if(m == 2){
        matriz_bidimensional();
    }
    else if(m == 2){
        matriz_tridimensional();
    }
    else{
        printf("Dimensão não suportada\n");
    }
    return 0;
}