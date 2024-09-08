function updateMatrix(mat: number[][]): number[][] {
	const m: number = mat.length, n: number = mat[0].length;
	const ans: number[][] = Array.from({length: m}, () => Array.from({length: n}, () => Number.MAX_SAFE_INTEGER >>> 1));
	for (let i: number = 0; i < m; i++) {
		for (let j: number = 0; j < n; j++) {
			if (mat[i][j] === 0) {
				ans[i][j] = 0;
			} else {
				if (i > 0) {
					ans[i][j] = Math.min(ans[i][j], ans[i - 1][j] + 1);
				}
				if (j > 0) {
					ans[i][j] = Math.min(ans[i][j], ans[i][j - 1] + 1);
				}
			}
		}
	}
	for (let i: number = m - 1; i >= 0; i--) {
		for (let j: number = n - 1; j >= 0; j--) {
			if (i < m - 1) {
				ans[i][j] = Math.min(ans[i][j], ans[i + 1][j] + 1);
			}
			if (j < n - 1) {
				ans[i][j] = Math.min(ans[i][j], ans[i][j + 1] + 1);
			}
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const mat: number[][] = JSON.parse(inputValues[0]);
	return updateMatrix(mat);
}
