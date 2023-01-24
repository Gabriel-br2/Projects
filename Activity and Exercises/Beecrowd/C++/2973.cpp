#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[]) {
    int n,c,t,x,m=0,mi,aux=1,ret;
    bool v = false;
    cin >> n >> c >> t;
    int s[n];
    for (int i = 0; i < n; i++){
        cin >> s[i];
        m = max(m,s[i]);
    }
    x = pow(2,(int) ceil(log2(m/t)));
    mi = x/2;
    while (aux != 0){
        int sa = 0;
        int cont = 0;
        for (int i = 0; i < n; i++){
            if (ceil(s[i]*1.0/t) > x || cont == c){
                cont = c+1;
                break;
            }
            if (ceil((double)(sa + s[i])/(t*1.0)) <= x){
                sa += s[i];
            } else {
                cont++;
                sa = s[i];
            }
        }
        cont++;
        aux = (x-mi)/2;
        if (cont <= c){
            ret = x;
            v = true;
            x -= aux;
        } else if (v){
            mi = x;
            x += aux;
        } else {
            aux = 1;
            mi = x;
            x = x*2;
        }
    }
    cout << ret << endl;
    return 0;
}