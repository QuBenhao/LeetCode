function generate(numRows: number): number[][] {
	const ans: number[][] = [[1]];
	for (let i: number = 1; i < numRows; i++) {
		const row: number[] = new Array(i + 1).fill(1);
		for (let j: number = 1; j < Math.floor(i / 2) + 1; j++) {
			row[j] = ans[i - 1][j - 1] + ans[i - 1][j];
			row[i - j] = row[j];
		}
		ans.push(row);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const numRows: number = JSON.parse(inputValues[0]);
	return generate(numRows);
}
