function minimumValueSum(nums: number[], andValues: number[]): number {
    const INF = (1 << 20) - 1;
    const n = nums.length, m = andValues.length;
    const memo = new Array(n * m).fill(null).map(() => new Map());

    function dfs(i, j, cur) {
        const key = i * andValues.length + j;
        if (i === nums.length && j === andValues.length) {
            return 0;
        }
        if (i === nums.length || j === andValues.length) {
            return INF;
        }
        if (memo[key].has(cur)) {
            return memo[key].get(cur);
        }

        cur &= nums[i];
        if ((cur & andValues[j]) < andValues[j]) {
            return INF;
        }
        let res = dfs(i + 1, j, cur);
        if (cur === andValues[j]) {
            res = Math.min(res, dfs(i + 1, j + 1, INF) + nums[i]);
        }
        memo[key].set(cur, res);
        return res;
    }

    const res = dfs(0, 0, INF);
    return res < INF ? res : -1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const andValues: number[] = JSON.parse(inputValues[1]);
	return minimumValueSum(nums, andValues);
}
