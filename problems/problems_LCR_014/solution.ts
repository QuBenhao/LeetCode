function checkInclusion(s1: string, s2: string): boolean {
	const cnt1: number[] = new Array(26).fill(0), cnt2: number[] = new Array(26).fill(0);
	const m: number = s1.length, n: number = s2.length;
	for (let i = 0; i < m; i++) {
		cnt1[s1.charCodeAt(i) - 97]++;
	}
	for (let i = 0; i < n; i++) {
		cnt2[s2.charCodeAt(i) - 97]++;
		if (i >= m - 1) {
			if (cnt1.toString() === cnt2.toString()) {
				return true;
			}
			cnt2[s2.charCodeAt(i - m + 1) - 97]--;
		}
	}
	return false;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s1: string = JSON.parse(inputValues[0]);
	const s2: string = JSON.parse(inputValues[1]);
	return checkInclusion(s1, s2);
}
