function getSmallestString(s: string): string {
	const n: number = s.length;
	for (let i: number = 0; i < n - 1; i++) {
		if (s[i] > s[i + 1] && parseInt(s[i]) % 2 === parseInt(s[i + 1]) % 2) {
			return s.substring(0, i) + s[i + 1] + s[i] + s.substring(i + 2);
		}
	}
	return s;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return getSmallestString(s);
}
