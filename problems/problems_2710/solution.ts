function removeTrailingZeros(num: string): string {

};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const num: string = JSON.parse(splits[0]);
	return removeTrailingZeros(num);
}
