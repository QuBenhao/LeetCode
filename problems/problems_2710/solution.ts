function removeTrailingZeros(num: string): string {
	let idx: number = num.length - 1;
	for (; idx >= 0 && num[idx] == '0'; idx--) {
	}
	return num.substring(0, idx + 1);
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const num: string = JSON.parse(splits[0]);
	return removeTrailingZeros(num);
}
