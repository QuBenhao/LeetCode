function minWindow(s: string, t: string): string {
    const charToIndex: Function = (c: string): number => c >= 'A' && c <= 'Z' ?
		c.charCodeAt(0) - 'A'.charCodeAt(0) : c.charCodeAt(0) - 'a'.charCodeAt(0) + 26;
	const count: number[] = new Array(52).fill(0), target: number[] = new Array(52).fill(0);
	let diff: number = 0, ansLeft: number = -1, ansRight: number = -1;
	for (let i: number = 0; i < t.length; i++) {
		const index: number = charToIndex(t[i]);
		if (target[index]++ === 0) diff++;
	}
	for (let left: number = 0, right: number = 0; right < s.length; right++) {
		const index: number = charToIndex(s[right]);
		if (++count[index] === target[index]) diff--;
		while (left < right) {
			const leftIndex: number = charToIndex(s[left]);
			if (count[leftIndex] > target[leftIndex] && --count[leftIndex] >= 0) {
				left++;
			} else {
				break;
			}
		}
		if (diff === 0 && (ansLeft === -1 || right - left < ansRight - ansLeft)) {
			ansLeft = left;
			ansRight = right;
		}
	}
	return ansLeft === -1 ? "" : s.substring(ansLeft, ansRight + 1);
};

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const s: string = JSON.parse(inputValues[0]);
    const t: string = JSON.parse(inputValues[1]);
    return minWindow(s, t);
}
