function isUnique(astr: string): boolean {
	let mask: number = 0;
	for (const ch of astr) {
		const cur: number = 1 << (ch.charCodeAt(0) - "a".charCodeAt(0));
		if ((mask & cur) !== 0) {
			return false;
		}
		mask |= cur;
	}
	return true;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const astr: string = JSON.parse(inputValues[0]);
	return isUnique(astr);
}
