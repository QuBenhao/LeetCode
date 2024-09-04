function combinationSum(candidates: number[], target: number): number[][] {
	const ans: number[][] = [];
	candidates.sort((a, b) => a - b);
	const backtrack = (start: number, target: number, path: number[]) => {
		if (target === 0) {
			ans.push(path.slice());
			return;
		}
		for (let i: number = start; i < candidates.length; i++) {
			if (target < candidates[i]) {
				break;
			}
			path.push(candidates[i]);
			backtrack(i, target - candidates[i], path);
			path.pop();
		}
	}
	backtrack(0, target, []);
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const candidates: number[] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return combinationSum(candidates, target);
}
