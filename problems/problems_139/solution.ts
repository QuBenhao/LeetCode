function wordBreak(s: string, wordDict: string[]): boolean {
    const words: Set<string> = new Set(wordDict);
	const n: number = s.length;
	const dp: boolean[] = Array(n + 1).fill(false);
	dp[0] = true;
	for (let i: number = 1; i <= n; i++) {
		for (let j: number = 0; j < i; j++) {
			if (dp[j] && words.has(s.substring(j, i))) {
				dp[i] = true;
				break;
			}
		}
	}
	return dp[n];
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const wordDict: string[] = JSON.parse(inputValues[1]);
	return wordBreak(s, wordDict);
}
