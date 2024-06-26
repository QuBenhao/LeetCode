function specialPerm(nums: number[]): number {
    const mod: number = 1e9 + 7;
    const n: number = nums.length;
    const m: number = 1 << n;
    const f: number[][] = Array.from({length: m}, () => Array(n).fill(0));

    for (let i: number = 1; i < m; ++i) {
        for (let j: number = 0; j < n; ++j) {
            if (((i >> j) & 1) === 1) {
                const ii = i ^ (1 << j);
                if (ii === 0) {
                    f[i][j] = 1;
                    continue;
                }
                for (let k: number = 0; k < n; ++k) {
                    if (nums[j] % nums[k] === 0 || nums[k] % nums[j] === 0) {
                        f[i][j] = (f[i][j] + f[ii][k]) % mod;
                    }
                }
            }
        }
    }

    return f[m - 1].reduce((acc, x) => (acc + x) % mod);
};

export function Solve(inputJsonElement: string): any {
    const splits: string[] = inputJsonElement.split("\n");
    const nums: number[] = JSON.parse(splits[0]);
    return specialPerm(nums);
}
