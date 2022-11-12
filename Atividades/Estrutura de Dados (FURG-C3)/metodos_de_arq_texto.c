#include <stdio.h>

int escrever_arq_C(){
    FILE *f = fopen("tc.txt","w");
    char i;
    for(i='a';i<='z';i++){
        fputc(i,f);
    }
    fclose(f);
    return 0;
}

int ler_arq_C(){
    FILE *f;
    char i;

    if((f = fopen("tc.txt","r"))==NULL){
        printf("Não foi possivel abrir o arquivo");
    }

    while((i=fgetc(f))!=EOF){
        printf("%c",i);
    }
    fclose(f);
    return 0;
}

int escrever_arq_S(){
    FILE *f = fopen("ts.txt","w");
    fputs("Escreve string 1 no arquivo.\n",f);
    fputs("Escreve string 2 no arquivo.\n",f);
    fputs("Escreve string 3 no arquivo.\n",f);
    fputs("Escreve string 4 no arquivo.\n",f);
    fputs("Escreve string 5 no arquivo.\n",f);
    fclose(f);
    return 0;
}

int ler_arq_S(){
    char palavra[100];
    FILE *f = fopen("ts.txt","r");
    while(fgets(palavra,100,f)!=NULL){
        printf("%s",palavra);
    }
    return 0;
}

int escrever_arq_I(){
    FILE *f = fopen("ti.txt","w");
    for(int i = 1; i<=10;i++){
        fprintf(f,"%d\n",i);
    }
    fclose(f);
}

int ler_arq_I(){
    FILE *f = fopen("ti.txt","r");
    int i;
    while(fscanf(f,"%d",&i)==1){
        printf("%d\n",i);
    }
    fclose(f);
}

int main(){
    escrever_arq_C();
    escrever_arq_S();
    escrever_arq_I();

    printf("----------------------------------\n");
    ler_arq_C();
    printf("\n----------------------------------\n");
    ler_arq_S();
    printf("----------------------------------\n");
    ler_arq_I();
    printf("----------------------------------\n");

    return 0;
}