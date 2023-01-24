#include <stdio.h>
#include <stdlib.h>

int main(){
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