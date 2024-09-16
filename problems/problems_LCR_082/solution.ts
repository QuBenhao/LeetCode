function combinationSum2(candidates: number[], target: number): number[][] {
	candidates.sort((a, b) => a - b);
	const result: number[][] = [];
	const dfs = (index: number, target: number, path: number[]) => {
		if (target < 0) {
			return;
		}
		if (target === 0) {
			result.push(path);
			return;
		}
		for (let i: number = index; i < candidates.length; i++) {
			if (i > index && candidates[i] === candidates[i - 1]) {
				continue;
			}
			dfs(i + 1, target - candidates[i], [...path, candidates[i]]);
		}
	};
	dfs(0, target, []);
	return result;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const candidates: number[] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return combinationSum2(candidates, target);
}
