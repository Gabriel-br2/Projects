#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	int N, M; int v[10005]; int C = 0;
	cin >> N >> M;
	for(int i = 1; i <= N; i++) cin >> v[i];
	priority_queue < pair <int,int> > fila;
	for(int i = 1; i <= N; i++) fila.push(make_pair(0,-i));
	while(M--){
		int c;
		cin >> c;
		int id = -fila.top().second;
		int l = -fila.top().first;
		fila.pop();
		fila.push(make_pair(-(l+v[id]*c),-id));
		C = max(C, l+v[id]*c); }
	printf("%d\n", C); }