function findAnagrams(s: string, p: string): number[] {
	const n: number = p.length;
	const count: Array<number> = new Array(26).fill(0);
	let diff: number = 0;
	for (let i: number = 0; i < n; i++) {
		if (count[p.charCodeAt(i) - 'a'.charCodeAt(0)]++ === 0) {
			diff++;
		}
	}
	const ans: Array<number> = [];
	for (let i: number = 0; i < s.length; i++) {
		const idx: number = s.charCodeAt(i) - 'a'.charCodeAt(0);
		count[idx]--;
		if (count[idx] === 0) {
			diff--;
		} else if (count[idx] === -1) {
			diff++;
		}
		if (i >= n - 1) {
			if (diff === 0) {
				ans.push(i - n + 1);
			}
			const old: number = s.charCodeAt(i - n + 1) - 'a'.charCodeAt(0);
			count[old]++;
			if (count[old] === 0) {
				diff--;
			} else if (count[old] === 1) {
				diff++;
			}
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const p: string = JSON.parse(inputValues[1]);
	return findAnagrams(s, p);
}
