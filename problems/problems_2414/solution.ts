function longestContinuousSubstring(s: string): number {
	const n: number = s.length;
	let ans: number = 1;
	for (let i: number = 0, cur: number = 1; i < n - 1; i++) {
		if (s.charCodeAt(i + 1) - s.charCodeAt(i) === 1) {
			cur++;
			ans = Math.max(ans, cur);
		} else {
			cur = 1;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return longestContinuousSubstring(s);
}
