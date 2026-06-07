/* ==========================================================
   Codigo criado por Claude Sonnet 4.6 - Anthropic
   Estrutura de Dados: Arvore AVL com menu interativo
   Operacoes: Inserir, Remover, Buscar, Listar, Info
   ========================================================== */

#include <stdio.h>
#include <stdlib.h>

/* ----------------------------------------------------------
   ESTRUTURA DO NO
   Cada no guarda:
   - valor inteiro
   - ponteiro para filho esquerdo e direito
   - altura (usada para calcular o fator de balanceamento)
   ---------------------------------------------------------- */
typedef struct No {
    int valor;
    struct No* esq;
    struct No* dir;
    int altura;
} No;


/* ==========================================================
   FUNCOES AUXILIARES
   ========================================================== */

/* Retorna a altura de um no. Se NULL, altura = 0 */
int altura(No* n) {
    if (n == NULL) return 0;
    return n->altura;
}

/* Retorna o maior entre dois inteiros */
int maximo(int a, int b) {
    return (a > b) ? a : b;
}

/* Cria um novo no com o valor informado */
No* criarNo(int valor) {
    No* novo    = (No*)malloc(sizeof(No));
    novo->valor  = valor;
    novo->esq    = NULL;
    novo->dir    = NULL;
    novo->altura = 1;   /* No folha tem altura 1 */
    return novo;
}

/* Atualiza a altura de um no com base nos seus filhos */
void atualizarAltura(No* n) {
    if (n != NULL)
        n->altura = 1 + maximo(altura(n->esq), altura(n->dir));
}

/* Fator de Balanceamento: altura(esq) - altura(dir)
   AVL exige que o resultado seja sempre -1, 0 ou +1 */
int fatorBalanceamento(No* n) {
    if (n == NULL) return 0;
    return altura(n->esq) - altura(n->dir);
}


/* ==========================================================
   ROTACOES
   ========================================================== */

/*
   ROTACAO SIMPLES A DIREITA — Caso Esquerda-Esquerda
   FB do no = +2  e  FB do filho esq = +1

        y                x
       / \              / \
      x   T3    →     T1   y
     / \                  / \
    T1  T2               T2  T3
*/
No* rotacaoDireita(No* y) {
    No* x  = y->esq;
    No* T2 = x->dir;

    x->dir = y;   /* x sobe, y desce para a direita */
    y->esq = T2;

    atualizarAltura(y);  /* y primeiro (ficou abaixo) */
    atualizarAltura(x);

    return x;  /* x e a nova raiz desta subarvore */
}

/*
   ROTACAO SIMPLES A ESQUERDA — Caso Direita-Direita
   FB do no = -2  e  FB do filho dir = -1

      x                  y
     / \                / \
    T1   y     →       x   T3
        / \           / \
       T2  T3        T1  T2
*/
No* rotacaoEsquerda(No* x) {
    No* y  = x->dir;
    No* T2 = y->esq;

    y->esq = x;   /* y sobe, x desce para a esquerda */
    x->dir = T2;

    atualizarAltura(x);
    atualizarAltura(y);

    return y;  /* y e a nova raiz desta subarvore */
}

/*
   ROTACAO DUPLA ESQUERDA-DIREITA — Caso Esquerda-Direita
   FB do no = +2  e  FB do filho esq = -1

   Passo 1: rotacao a esquerda no filho esquerdo
   Passo 2: rotacao a direita no no desbalanceado
*/
No* rotacaoEsquerdaDireita(No* z) {
    z->esq = rotacaoEsquerda(z->esq);  /* Passo 1 */
    return rotacaoDireita(z);          /* Passo 2 */
}

/*
   ROTACAO DUPLA DIREITA-ESQUERDA — Caso Direita-Esquerda
   FB do no = -2  e  FB do filho dir = +1

   Passo 1: rotacao a direita no filho direito
   Passo 2: rotacao a esquerda no no desbalanceado
*/
No* rotacaoDireitaEsquerda(No* z) {
    z->dir = rotacaoDireita(z->dir);  /* Passo 1 */
    return rotacaoEsquerda(z);        /* Passo 2 */
}


/* ==========================================================
   BALANCEAMENTO
   Verifica o FB e aplica a rotacao correta se necessario
   ========================================================== */
No* balancear(No* n) {
    atualizarAltura(n);

    int fb = fatorBalanceamento(n);

    /* CASO 1: Esq-Esq → Rotacao Simples Direita */
    if (fb == 2 && fatorBalanceamento(n->esq) >= 0)
        return rotacaoDireita(n);

    /* CASO 2: Esq-Dir → Rotacao Dupla Esq-Dir */
    if (fb == 2 && fatorBalanceamento(n->esq) < 0)
        return rotacaoEsquerdaDireita(n);

    /* CASO 3: Dir-Dir → Rotacao Simples Esquerda */
    if (fb == -2 && fatorBalanceamento(n->dir) <= 0)
        return rotacaoEsquerda(n);

    /* CASO 4: Dir-Esq → Rotacao Dupla Dir-Esq */
    if (fb == -2 && fatorBalanceamento(n->dir) > 0)
        return rotacaoDireitaEsquerda(n);

    return n;  /* Ja esta balanceado */
}


/* ==========================================================
   INSERCAO
   Igual a BST, mas com balanceamento automatico ao final
   ========================================================== */
No* inserir(No* raiz, int valor) {
    /* Posicao encontrada: cria o novo no */
    if (raiz == NULL)
        return criarNo(valor);

    if (valor < raiz->valor)
        raiz->esq = inserir(raiz->esq, valor);
    else if (valor > raiz->valor)
        raiz->dir = inserir(raiz->dir, valor);
    else {
        /* Valor duplicado: AVL nao permite */
        printf("  [!] Valor %d ja existe na arvore!\n", valor);
        return raiz;
    }

    /* Corrige o balanceamento ao voltar da recursao */
    return balancear(raiz);
}


/* ==========================================================
   REMOCAO
   ========================================================== */

/* Encontra o menor no de uma subarvore (mais a esquerda) */
No* menorNo(No* n) {
    while (n->esq != NULL)
        n = n->esq;
    return n;
}

No* remover(No* raiz, int valor) {
    if (raiz == NULL) {
        printf("  [!] Valor %d nao encontrado na arvore!\n", valor);
        return NULL;
    }

    /* Busca o no a remover */
    if (valor < raiz->valor)
        raiz->esq = remover(raiz->esq, valor);
    else if (valor > raiz->valor)
        raiz->dir = remover(raiz->dir, valor);
    else {
        /* No encontrado — 3 casos possiveis: */

        /* Caso 1: no folha (sem filhos) — remove diretamente */
        if (raiz->esq == NULL && raiz->dir == NULL) {
            free(raiz);
            return NULL;
        }
        /* Caso 2a: so tem filho direito */
        else if (raiz->esq == NULL) {
            No* temp = raiz->dir;
            free(raiz);
            return temp;
        }
        /* Caso 2b: so tem filho esquerdo */
        else if (raiz->dir == NULL) {
            No* temp = raiz->esq;
            free(raiz);
            return temp;
        }
        /* Caso 3: tem dois filhos
           Substitui pelo sucessor (menor da subarvore direita)
           e remove o sucessor de la */
        else {
            No* sucessor = menorNo(raiz->dir);
            raiz->valor  = sucessor->valor;
            raiz->dir    = remover(raiz->dir, sucessor->valor);
        }
    }

    /* Corrige o balanceamento ao voltar da recursao */
    return balancear(raiz);
}


/* ==========================================================
   BUSCA — O(log n)
   ========================================================== */
No* buscar(No* raiz, int valor) {
    if (raiz == NULL) return NULL;         /* Nao encontrou */
    if (valor == raiz->valor) return raiz; /* Encontrou! */

    if (valor < raiz->valor)
        return buscar(raiz->esq, valor);
    else
        return buscar(raiz->dir, valor);
}


/* ==========================================================
   TRAVESSIAS
   ========================================================== */

/* Em-ordem: Esq → Raiz → Dir  (resultado em ordem crescente) */
void emOrdem(No* raiz) {
    if (raiz != NULL) {
        emOrdem(raiz->esq);
        printf("%d ", raiz->valor);
        emOrdem(raiz->dir);
    }
}

/* Pre-ordem: Raiz → Esq → Dir */
void preOrdem(No* raiz) {
    if (raiz != NULL) {
        printf("%d ", raiz->valor);
        preOrdem(raiz->esq);
        preOrdem(raiz->dir);
    }
}

/* Pos-ordem: Esq → Dir → Raiz */
void posOrdem(No* raiz) {
    if (raiz != NULL) {
        posOrdem(raiz->esq);
        posOrdem(raiz->dir);
        printf("%d ", raiz->valor);
    }
}

/* Conta quantos nos existem na arvore */
int contarNos(No* raiz) {
    if (raiz == NULL) return 0;
    return 1 + contarNos(raiz->esq) + contarNos(raiz->dir);
}


/* ==========================================================
   MENU INTERATIVO
   ========================================================== */

void exibirCabecalho() {
    printf("\n");
    printf("  ╔══════════════════════════════════════╗\n");
    printf("  ║         ARVORE AVL INTERATIVA        ║\n");
    printf("  ║   Criado por Claude Sonnet 4.6       ║\n");
    printf("  ║           Anthropic - 2025           ║\n");
    printf("  ╚══════════════════════════════════════╝\n");
    printf("\n");
}

void exibirMenu() {
    printf("  ┌──────────────────────────────────────┐\n");
    printf("  │              MENU PRINCIPAL           │\n");
    printf("  ├──────────────────────────────────────┤\n");
    printf("  │  1. Inserir valor                    │\n");
    printf("  │  2. Remover valor                    │\n");
    printf("  │  3. Buscar valor                     │\n");
    printf("  │  4. Listar em-ordem (crescente)      │\n");
    printf("  │  5. Listar pre-ordem                 │\n");
    printf("  │  6. Listar pos-ordem                 │\n");
    printf("  │  7. Informacoes da arvore            │\n");
    printf("  │  0. Sair                             │\n");
    printf("  └──────────────────────────────────────┘\n");
    printf("  Opcao: ");
}

void exibirInfo(No* raiz) {
    printf("\n  ╔══════════════════════════════════════╗\n");
    printf("  ║         INFORMACOES DA ARVORE        ║\n");
    printf("  ╠══════════════════════════════════════╣\n");

    if (raiz == NULL) {
        printf("  ║   Arvore vazia!                      ║\n");
    } else {
        printf("  ║  Raiz          : %-20d║\n", raiz->valor);
        printf("  ║  Altura total  : %-20d║\n", altura(raiz));
        printf("  ║  Total de nos  : %-20d║\n", contarNos(raiz));
        printf("  ║  FB da raiz    : %-20d║\n", fatorBalanceamento(raiz));
        printf("  ║  Complexidade  : O(log n)            ║\n");
    }

    printf("  ╚══════════════════════════════════════╝\n");
}


/* ==========================================================
   FUNCAO PRINCIPAL
   ========================================================== */
int main() {
    No* raiz  = NULL;
    int opcao = -1;
    int valor;
    No* resultado;

    exibirCabecalho();

    /* Loop principal do menu */
    while (opcao != 0) {

        exibirMenu();
        scanf("%d", &opcao);

        switch (opcao) {

            /* -------- INSERIR -------- */
            case 1:
                printf("\n  Digite o valor a inserir: ");
                scanf("%d", &valor);
                raiz = inserir(raiz, valor);
                printf("  [OK] Valor %d inserido!\n", valor);
                break;

            /* -------- REMOVER -------- */
            case 2:
                if (raiz == NULL) {
                    printf("\n  [!] Arvore vazia!\n");
                    break;
                }
                printf("\n  Digite o valor a remover: ");
                scanf("%d", &valor);
                raiz = remover(raiz, valor);
                if (raiz != NULL || valor == raiz->valor)
                    printf("  [OK] Valor %d removido!\n", valor);
                break;

            /* -------- BUSCAR -------- */
            case 3:
                if (raiz == NULL) {
                    printf("\n  [!] Arvore vazia!\n");
                    break;
                }
                printf("\n  Digite o valor a buscar: ");
                scanf("%d", &valor);
                resultado = buscar(raiz, valor);
                if (resultado)
                    printf("  [OK] Valor %d encontrado! | Altura do no: %d | FB: %d\n",
                           valor, resultado->altura, fatorBalanceamento(resultado));
                else
                    printf("  [!] Valor %d nao encontrado.\n", valor);
                break;

            /* -------- EM-ORDEM -------- */
            case 4:
                if (raiz == NULL) {
                    printf("\n  [!] Arvore vazia!\n");
                    break;
                }
                printf("\n  Em-ordem (crescente): ");
                emOrdem(raiz);
                printf("\n");
                break;

            /* -------- PRE-ORDEM -------- */
            case 5:
                if (raiz == NULL) {
                    printf("\n  [!] Arvore vazia!\n");
                    break;
                }
                printf("\n  Pre-ordem: ");
                preOrdem(raiz);
                printf("\n");
                break;

            /* -------- POS-ORDEM -------- */
            case 6:
                if (raiz == NULL) {
                    printf("\n  [!] Arvore vazia!\n");
                    break;
                }
                printf("\n  Pos-ordem: ");
                posOrdem(raiz);
                printf("\n");
                break;

            /* -------- INFORMACOES -------- */
            case 7:
                exibirInfo(raiz);
                break;

            /* -------- SAIR -------- */
            case 0:
                printf("\n  Encerrando... Obrigado!\n\n");
                break;

            /* -------- OPCAO INVALIDA -------- */
            default:
                printf("\n  [!] Opcao invalida! Digite um numero entre 0 e 7.\n");
                break;
        }

        printf("\n");
    }

    return 0;
}