//
// Created by benhao on 2025/12/23.
//

#include <cstdio>
#include <vector>
using namespace std;

// Add v to each element from [x1, y1] to [x2, y2].
void add(vector<vector<int> > &diff, int n, int m, int x1, int y1, int x2, int y2, int v) {
    diff[x1][y1] += v;
    if (x2 < n) diff[x2 + 1][y1] -= v;
    if (y2 < m) diff[x1][y2 + 1] -= v;
    if (x2 < n && y2 < m) diff[x2 + 1][y2 + 1] += v;
}

// Execute this after all modifications and before all queries.
void prefix_sum(const vector<vector<int> > &diff, vector<vector<int> >& a, int n, int m) {
    a = diff;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) a[i][j] += a[i - 1][j];

    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) a[i][j] += a[i][j - 1];
}

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    vector matrix(n + 1, vector<int>(n + 1, 0));
    for (int i = 0; i < m; ++i) {
        int x1, x2, y1, y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        add(matrix, n, n, x1, y1, x2, y2, 1);
    }
    vector<vector<int> > a;
    prefix_sum(matrix, a, n, n);
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (j < n) {
                printf("%d ", a[i][j]);
            } else {
                printf("%d\n", a[i][j]);
            }
        }
    }
    return 0;
}
