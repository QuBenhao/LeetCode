function isAnagram(s: string, t: string): boolean {
	if (s.length !== t.length || s === t) {
		return false;
	}
	const cnt: number[] = new Array(26).fill(0);
	for (let i: number = 0; i < s.length; i++) {
		cnt[s.charCodeAt(i) - "a".charCodeAt(0)]++;
		cnt[t.charCodeAt(i) - "a".charCodeAt(0)]--;
	}
	for (let i: number = 0; i < 26; i++) {
		if (cnt[i] !== 0) {
			return false;
		}
	}
	return true;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const t: string = JSON.parse(inputValues[1]);
	return isAnagram(s, t);
}
