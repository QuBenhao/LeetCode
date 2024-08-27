function partition(s: string): string[][] {
	const n: number = s.length;
	const dp: boolean[][] = new Array(n);
	for (let i: number = 0; i < n; i++) {
		dp[i] = new Array(n).fill(false);
		dp[i][i] = true;
	}
	for (let i: number = 0; i < n; i++) {
		for (let j: number = 0; j <= i; j++) {
			if (s[i] === s[j] && (i - j <= 1 || dp[j + 1][i - 1])) {
				dp[j][i] = true;
			}
		}
	}
	const res: string[][] = [];
	const path: string[] = [];
	const dfs = (i: number): void => {
		if (i === n) {
			res.push([...path]);
			return;
		}
		for (let j: number = i; j < n; j++) {
			if (dp[i][j]) {
				path.push(s.slice(i, j + 1));
				dfs(j + 1);
				path.pop();
			}
		}
	};
	dfs(0);
	return res;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return partition(s);
}
