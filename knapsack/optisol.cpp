#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <chrono>
using namespace std;

map<pair<int,int>, int> memoria;

int Mochila(vector<int>& p, vector<int>& v, int n, int C) {
    if (n == 0 || C == 0) return 0;
    if (p[n - 1] > C) return Mochila(p, v, n - 1, C);
    auto key = make_pair(C, n);
    if (memoria.count(key)) return memoria[key];
    int valor_tomado   = v[n - 1] + Mochila(p, v, n - 1, C - p[n - 1]);
    int valor_notomado = Mochila(p, v, n - 1, C);
    int valor_max      = max(valor_tomado, valor_notomado);
    memoria[key] = valor_max;
    return valor_max;
}

int Mochila_Bt(vector<int>& p, vector<int>& v, int n, int C,
               int i = 0, int p_act = 0, int v_act = 0) {
    if (i == n) return v_act;
    int max_valor = Mochila_Bt(p, v, n, C, i + 1, p_act, v_act);
    if (p_act + p[i] <= C)
        max_valor = max(max_valor,
                        Mochila_Bt(p, v, n, C, i + 1, p_act + p[i], v_act + v[i]));
    return max_valor;
}

struct Instancia { int ejemplo, n, C; vector<int> p, v; };
struct Resultado  { int ejemplo, n, C, valor; double tiempo; };

int main() {
    vector<Instancia> instancias = {
        {1,  9, 25, {6,4,8,4,3,5,5,1,1},    {6,12,18,19,4,3,17,3,15}},
        {2,  9, 26, {8,2,3,5,7,4,4,1,3},    {4,17,14,12,12,9,10,20,7}},
        {3,  7, 13, {6,8,9,9,8,6,4},         {18,6,17,12,13,10,14}},
        {4, 10, 12, {7,1,8,5,8,5,3,3,1,9},  {17,18,14,12,2,11,1,14,1,19}},
        {5,  9, 30, {9,2,4,4,10,7,10,3,5},  {4,8,5,19,12,20,1,4,9}},
        {6,  8, 27, {10,10,1,4,6,2,2,7},     {16,17,7,3,12,17,8,2}},
        {7,  7, 28, {1,3,6,4,7,9,6},         {16,2,19,6,17,8,20}},
        {8,  6, 26, {7,8,2,5,6,10},          {18,12,13,19,15,11}},
        {9,  5, 11, {4,4,4,3,1},             {17,4,9,1,9}},
        {10, 9, 26, {9,1,7,3,7,5,1,5,4},    {13,5,17,6,12,12,20,9,20}},
    };

    cout << "INSTANCIAS GENERADAS\n";
    for (auto& inst : instancias) {
        cout << "\nEjemplo " << inst.ejemplo << "\n";
        cout << "n: " << inst.n << "\n";
        cout << "Pesos: [";
        for (int i = 0; i < inst.n; i++) cout << inst.p[i] << (i+1<inst.n?", ":"");
        cout << "]\nValores: [";
        for (int i = 0; i < inst.n; i++) cout << inst.v[i] << (i+1<inst.n?", ":"");
        cout << "]\nCapacidad: " << inst.C << "\n";
    }

    vector<Resultado> res_dp, res_bt;
    for (auto& inst : instancias) {
        memoria.clear();
        auto t1 = chrono::high_resolution_clock::now();
        int val_dp = Mochila(inst.p, inst.v, inst.n, inst.C);
        auto t2 = chrono::high_resolution_clock::now();
        res_dp.push_back({inst.ejemplo, inst.n, inst.C, val_dp,
                          chrono::duration<double>(t2-t1).count()});

        auto t3 = chrono::high_resolution_clock::now();
        int val_bt = Mochila_Bt(inst.p, inst.v, inst.n, inst.C);
        auto t4 = chrono::high_resolution_clock::now();
        res_bt.push_back({inst.ejemplo, inst.n, inst.C, val_bt,
                          chrono::duration<double>(t4-t3).count()});
    }

    cout << "\n=== DP ===\n";
    for (auto& r : res_dp)
        printf("Ejemplo %d | n=%d | C=%d | Tiempo: %.6f s | Resultado: %d\n",
               r.ejemplo, r.n, r.C, r.tiempo, r.valor);

    cout << "\n=== Backtracking ===\n";
    for (auto& r : res_bt)
        printf("Ejemplo %d | n=%d | C=%d | Tiempo: %.6f s | Resultado: %d\n",
               r.ejemplo, r.n, r.C, r.tiempo, r.valor);

    return 0;
}