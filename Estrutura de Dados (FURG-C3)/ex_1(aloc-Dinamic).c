#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    float *vetor, total=0;

    printf("Quantas notas deseja inserir: ");
    scanf("%d",&n);

    vetor = calloc(n,sizeof(float));
    for(int a = 0; a<n; a++){
        printf("valor de vetor[%d]: ",a);
        scanf("%f", &vetor[a]);
        total += vetor[a];
    }
    printf("A média é %.2f\n", total/n);
    free(vetor);

    return 0;
}