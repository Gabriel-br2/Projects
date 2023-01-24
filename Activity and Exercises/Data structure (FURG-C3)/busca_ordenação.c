#include <stdio.h>
#include <stdlib.h>

//busca binario com Bubble Sort e selection

int Busca_bin(int vet[], int fim ,int busca){
    int ini = 0;
    while (ini < fim){
        int meio = ((ini +fim)/2);
        if(vet[meio]==busca){
            ini = fim+1;
            return meio;
        }
        else{
            if(vet[meio]>busca){
                fim = meio;
            }
            if(vet[meio]<busca){
                ini = meio;
            }
        }
    }
    return -1;
}

int ordenar_bb(int vet[10],int t){
	int aux;
	for(int j=t-1; j>=1; j--){
		for(int i=0; i<j; i++){
			if(vet[i]>vet[i+1]){
				aux=vet[i];
                vet[i]=vet[i+1];
                vet[i+1]=aux;
            }
        }
    }
}

void ordenar_sel( int vet[], int t){ 
	int pm, temp;
	for (int i = 0; i<(t-1); i++){ 
		pm = i; 
		for (int j = (i + 1); j<t; j++){ 			
			if(vet[j] < vet[pm]){ 
				pm = j; 
		    }
		    if (i != pm){
                temp = vet[i];
	            vet[i] = vet[pm];
	            vet[pm] = temp;
		    }
	    }
    }
}

int main(){
    int *vet, tam, bb,s,a;

    printf("Tamanho do vetor: ");scanf("%d",&tam);

    vet = (int *)malloc(tam*sizeof(int*));
    for(int a = 0; a<tam;a++){
        printf("Entre com o valor de vet[%d]: ",a);scanf("%d",&vet[a]);
    }

    printf("Metodo de ordenação - Bubble sort(1) ou Selection sort(2): ");
    scanf("%d",&s);

    if (s==1){ordenar_bb(vet,tam);}
    if (s==2){ordenar_sel(vet,tam);}
    
    printf("valor a ser buscado: ");scanf("%d",&bb);

    a = Busca_bin(vet,tam,bb);

    if(a == -1){
        printf("Valor n encontrado\n");
    }
    else{
        printf("\n");
        printf("Valor encontrado na posição: %d\n",a);

    }
    
    return 0;
}