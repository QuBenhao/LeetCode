function combine(n: number, k: number): number[][] {
	const ans: number[][] = [];
	const backtrack = (start: number, path: number[]): void => {
		if (path.length === k) {
			ans.push([...path]);
			return;
		}
		for (let i = start; i <= n; i++) {
			path.push(i);
			backtrack(i + 1, path);
			path.pop();
		}
	}
	backtrack(1, []);
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return combine(n, k);
}
