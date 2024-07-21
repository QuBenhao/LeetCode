function letterCombinations(digits: string): string[] {
    const translator: string[] = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];
	const result: string[] = [];
	const dfs: Function = (index: number, path: string): void => {
		if (index === digits.length) {
			result.push(path);
			return;
		}
		for (const c of translator[digits.charCodeAt(index) - "2".charCodeAt(0)]) {
			dfs(index + 1, path + c);
		}
	};
	if (digits.length > 0) {
		dfs(0, "");
	}
	return result;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const digits: string = JSON.parse(inputValues[0]);
	return letterCombinations(digits);
}
