function maximumSubsequenceCount(text: string, pattern: string): number {
    let ans: number = 0, p0: number = 0, p1: number = 0;
	for (const c of text) {
		if (c === pattern[1]) {
			ans += p0;
			p1++;
		}
		if (c === pattern[0]) {
			p0++;
		}
	}
	return ans + Math.max(p0, p1);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const text: string = JSON.parse(inputValues[0]);
	const pattern: string = JSON.parse(inputValues[1]);
	return maximumSubsequenceCount(text, pattern);
}
