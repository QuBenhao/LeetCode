//
// Created by benhao on 2025/12/26.
//

#include <bits/stdc++.h>
using namespace std;

int N;
double A[20];
constexpr double eps = 1e-7;

double fx(double x) {
    double r = 0;
    for (int i = N; i >= 0; --i) {
        r += A[i] * pow(x, i);
    }
    return r;
}

int main() {
    double l, r;
    cin >> N >> l >> r;
    for (int i = N; i >= 0; --i) {
        cin >> A[i];
    }
    while (r - l > eps) {
        double mid = (l + r) / 2;
        double lmid = mid - eps;
        double rmid = mid + eps;
        if (fx(lmid) > fx(rmid)) {
            r = lmid;
        } else {
            l = rmid;
        }
    }
    cout << l << endl;
    return 0;
}