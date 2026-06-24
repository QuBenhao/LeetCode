import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.zigZagArrays(*test_input)

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1  # number of possible values
        if n == 1:
            return m
        if n == 2:
            return m * (m - 1)

        # State: idx(v, d) where v in [l,r], d in {0: down, 1: up}
        # idx = (v - l) * 2 + d
        state_size = 2 * m

        def idx(v, d):
            return (v - l) * 2 + d

        # Build transition matrix T
        # T[i][j] = 1 means transition from state j to state i
        # State: idx(v, d) where v in [l,r], d in {0: down to v, 1: up to v}
        T = [[0] * state_size for _ in range(state_size)]
        for v in range(l, r + 1):
            for d in range(2):
                for w in range(l, r + 1):
                    if w == v:
                        continue
                    if d == 0 and w > v:  # was down to v, now up to w
                        T[idx(w, 1)][idx(v, 0)] = 1
                    elif d == 1 and w < v:  # was up to v, now down to w
                        T[idx(w, 0)][idx(v, 1)] = 1

        # Initial vector for position 2
        # init[idx(v, 0)] = count of prev > v = r - v
        # init[idx(v, 1)] = count of prev < v = v - l
        init = [0] * state_size
        for v in range(l, r + 1):
            init[idx(v, 0)] = max(0, r - v)  # prev in [v+1, r]
            init[idx(v, 1)] = max(0, v - l)  # prev in [l, v-1]

        # Matrix-vector multiplication
        def mat_vec_mul(T, vec):
            n = len(T)
            result = [0] * n
            for i in range(n):
                s = 0
                row = T[i]
                for j in range(n):
                    if row[j]:
                        s = (s + row[j] * vec[j]) % MOD
                result[i] = s
            return result

        # Matrix multiplication
        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                Ai = A[i]
                Ci = C[i]
                for k in range(n):
                    aik = Ai[k]
                    if aik:
                        Bk = B[k]
                        for j in range(n):
                            Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        # Matrix exponentiation: T^k
        def mat_pow(T, k):
            n = len(T)
            # Identity matrix
            result = [[0] * n for _ in range(n)]
            for i in range(n):
                result[i][i] = 1
            base = T
            while k > 0:
                if k & 1:
                    result = mat_mul(result, base)
                base = mat_mul(base, base)
                k >>= 1
            return result

        # Compute T^(n-2) * init
        Tk = mat_pow(T, n - 2)
        final = mat_vec_mul(Tk, init)

        return sum(final) % MOD

MOD = 10**9 + 7
