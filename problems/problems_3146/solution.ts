function findPermutationDifference(s: string, t: string): number {
	const idxes: Array<number> = new Array<number>(26).fill(0);
	for (let i = 0; i < s.length; i++) {
		idxes[s.charCodeAt(i) - "a".charCodeAt(0)] += i;
		idxes[t.charCodeAt(i) - "a".charCodeAt(0)] -= i;
	}
	let ans: number = 0;
	for (const idx of idxes) {
		ans += Math.abs(idx);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const t: string = JSON.parse(inputValues[1]);
	return findPermutationDifference(s, t);
}
