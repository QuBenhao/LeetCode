function minWindow(s: string, t: string): string {
	const n: number = s.length;
	let ansLeft: number = -1, ansRight: number = -1;
	let left: number = 0, right: number = 0;
	const counter: Map<string, number> = new Map<string, number>();
	for (const c of t) {
		counter.set(c, (counter.get(c) || 0) + 1);
	}
	let diff: number = counter.size;
	while (right < n) {
		const c: string = s[right];
		if (counter.has(c)) {
			counter.set(c, counter.get(c) - 1);
			if (counter.get(c) === 0) {
				diff--;
			}
		}
		right++;
		while (diff === 0) {
			if (ansLeft === -1 || right - left < ansRight - ansLeft) {
				ansLeft = left;
				ansRight = right;
			}
			const c: string = s[left];
			if (counter.has(c)) {
				counter.set(c, counter.get(c) + 1);
				if (counter.get(c) === 1) {
					diff++;
				}
			}
			left++;
		}
	}
	return ansLeft === -1 ? "" : s.substring(ansLeft, ansRight);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const t: string = JSON.parse(inputValues[1]);
	return minWindow(s, t);
}
