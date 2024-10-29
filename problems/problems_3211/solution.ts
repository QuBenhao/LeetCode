function validStrings(n: number): string[] {
    const ans: string[] = [];
	const path: string[] = new Array(n).fill("");
	const dfs = (i: number): void => {
		if (i === n) {
			ans.push(path.join(""));
			return;
		}
		if (i == 0 || path[i - 1] === '1') {
			path[i] = '0';
			dfs(i + 1);
		}
		path[i] = '1';
		dfs(i + 1);
	}
	dfs(0);
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return validStrings(n);
}
