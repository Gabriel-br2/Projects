#include <stdio.h>

int main(){
    FILE *f1 = fopen("arq1.txt","r");
    FILE *f2 = fopen("arq2.txt","w");
    
    int i = 0;
    char p[100];
    
    while(fscanf(f1,"%s",p)==1){
        fprintf(f2,"%s",p);
        i++;
        if((i%6)==0){
            fputc('\n',f2);
        }
    }
    fclose(f1);
    fclose(f2);

}