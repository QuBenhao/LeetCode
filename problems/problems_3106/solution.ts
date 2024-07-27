function getSmallestString(s: string, k: number): string {
    const distance = (a: string, b: string) => {
        return Math.min((b.charCodeAt(0) - a.charCodeAt(0) + 26) % 26, (a.charCodeAt(0) - b.charCodeAt(0) + 26) % 26);
    }
	let idx: number = 0;
	const result: string[] = [];
	while (idx < s.length && k > 0) {
		if (s.charAt(idx) === 'a') {
			result.push('a');
		} else {
			const d: number = distance('a', s.charAt(idx));
			if (d <= k) {
				result.push('a');
				k -= d;
			} else {
				result.push(String.fromCharCode(s.charCodeAt(idx) - k));
				k = 0;
			}
		}
		idx++;
	}
	result.push(s.substring(idx));
	return result.join('');
};

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const s: string = JSON.parse(inputValues[0]);
    const k: number = JSON.parse(inputValues[1]);
    return getSmallestString(s, k);
}
