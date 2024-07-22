function maximumSum(arr: number[]): number {
    let ans: number = -Infinity, dp0: number = -Infinity, dp1: number = -Infinity;
	for (const num of arr) {
		dp1 = Math.max(dp1 + num, dp0);
		dp0 = Math.max(dp0 + num, num);
		ans = Math.max(ans, dp1, dp0);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const arr: number[] = JSON.parse(inputValues[0]);
	return maximumSum(arr);
}
