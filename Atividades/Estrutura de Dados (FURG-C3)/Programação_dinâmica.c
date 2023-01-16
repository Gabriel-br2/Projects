#include <stdio.h>
#include <string.h>
#include <time.h> 

long int tabela_td[100];
long int tabela_bu[100];
int tam = 2;

int fib(int n){
  if ((n == 0) || (n == 1))
    return n;
  return fib(n-1) + fib(n-2);
}

long int fibBottomUp(long int n){
  tabela_bu[0] = 0;
  tabela_bu[1] = 1;
  for(int count = 2;count < n+1;count++){
    tabela_bu[count] = tabela_bu[count-1] + tabela_bu[count-2];  
  }
  return tabela_bu[n];
}

long int fibTopDown(long int n){
  if ((n == 1) || (n == 0))
    return n;
  if (n < tam)
    return tabela_td[n-2];
  tabela_td[n-2] = fibTopDown(n-1) + fibTopDown(n-2);
  tam++;
  return tabela_td[n-2];  
}

void test_tempo_func(int op, int n){
    char op_t[50];
    double resultado_tempo = 0.0;
    long int result;
    
    clock_t temp_start = clock();
    if (op == 0){
        result = fib(n);
        strcpy(op_t, "Original");
    }
    else if (op == 1){
        result = fibBottomUp(n);
        strcpy(op_t, "BottomUp");
    }
    else if (op == 2){
        result = fibTopDown(n);
        strcpy(op_t, "Top-Down");
    }
    clock_t temp_finish = clock();
    
    resultado_tempo = (double)(temp_finish - temp_start) / CLOCKS_PER_SEC;
    printf("Resultado - Fibonacci (%s): %ld\n",op_t,result);
    printf("Tempo de Execução - Fibonacci (%s): %.7f\n",op_t,resultado_tempo);
    printf("===================================================\n");  
}

int main() {
  int n = 35;
  // 0 = Original; 1 = BottomUp; 2 = TopDown
  printf("===================================================\n");
  test_tempo_func(0,n);
  test_tempo_func(1,n);
  test_tempo_func(2,n);
  return 0;
}