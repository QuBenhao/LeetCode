function combinationSum(candidates: number[], target: number): number[][] {
	const ans: number[][] = [];
	const path: number[] = [];
    const dfs: Function = (index: number, s: number) => {
		if (s === 0) {
			ans.push([...path]);
			return;
		}
		if (index === candidates.length) {
			return;
		}
		if (candidates[index] <= s) {
			path.push(candidates[index]);
			dfs(index, s - candidates[index]);
			path.pop();
		}
		dfs(index + 1, s);
	};
	dfs(0, target);
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const candidates: number[] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return combinationSum(candidates, target);
}
