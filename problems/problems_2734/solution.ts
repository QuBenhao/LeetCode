function smallestString(s: string): string {

};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(splits[0]);
	return smallestString(s);
}
