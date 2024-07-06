function lengthOfLongestSubstring(s: string): number {
	const map: Map<string, number> = new Map<string, number>();
	let ans: number = 0;
	for (let i: number = 0, j: number = -1; i < s.length; i++) {
		if (map.has(s[i])) {
			j = Math.max(map.get(s[i]), j);
		}
		ans = Math.max(ans, i - j);
		map.set(s[i], i);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return lengthOfLongestSubstring(s);
}
