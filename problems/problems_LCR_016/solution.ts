function lengthOfLongestSubstring(s: string): number {
	const explored: Set<string> = new Set<string>();
	let ans: number = 0;
	for (let left: number = 0, right: number = 0; right < s.length; right++) {
		while (explored.has(s[right])) {
			explored.delete(s[left]);
			left++;
		}
		explored.add(s[right]);
		ans = Math.max(ans, right - left + 1);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return lengthOfLongestSubstring(s);
}
