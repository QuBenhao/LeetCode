function findAnagrams(s: string, p: string): number[] {
	const m: number = s.length, n: number = p.length;
	const counter: number[] = new Array<number>(26).fill(0);
	for (let i: number = 0; i < n; i++) {
		counter[p.charCodeAt(i) - 97]--;
	}
	let diff: number = 0;
	for (let i: number = 0; i < 26; i++) {
		if (counter[i] !== 0) {
			diff++;
		}
	}
	const helper: Function = (key: number, val: number)=> {
		const before: boolean = counter[key] === 0;
		counter[key] += val;
		if (before) {
			return 1;
		}
		if (counter[key] === 0) {
			return -1;
		}
		return 0;
	}
	const ans: number[] = [];
	for (let i: number = 0; i < m; i++) {
		diff += helper(s.charCodeAt(i) - 97, 1);
		if (i >= n - 1) {
			if (diff === 0) {
				ans.push(i - n + 1);
			}
			diff += helper(s.charCodeAt(i - n + 1) - 97, -1);
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
