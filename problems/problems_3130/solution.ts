function numberOfStableArrays(zero: number, one: number, limit: number): number {
    const mod: number = 1000000007;
    const dp: Array<Array<Array<number>>> = new Array<Array<Array<number>>>(zero + 1);
    for (let i: number = 0; i < zero + 1; i++) {
        dp[i] = new Array<Array<number>>(one + 1);
        for (let j: number = 0; j < one + 1; j++) {
            dp[i][j] = new Array<number>(2).fill(0);
        }
    }
    for (let i: number = 1; i <= Math.min(zero, limit); i++) {
        dp[i][0][0] = 1;
    }
    for (let i: number = 1; i <= Math.min(one, limit); i++) {
        dp[0][i][1] = 1;
    }
    for (let i: number = 1; i <= zero; i++) {
        for (let j: number = 1; j <= one; j++) {
            dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod;
            if (i > limit) {
                dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + mod) % mod;
            }
            dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % mod;
            if (j > limit) {
                dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + mod) % mod;
            }
        }
    }
    return (dp[zero][one][0] + dp[zero][one][1]) % mod;
};

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const zero: number = JSON.parse(inputValues[0]);
    const one: number = JSON.parse(inputValues[1]);
    const limit: number = JSON.parse(inputValues[2]);
    return numberOfStableArrays(zero, one, limit);
}
