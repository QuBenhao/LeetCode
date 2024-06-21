function smallestBeautifulString(s: string, k: number): string {

};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(splits[0]);
	const k: number = JSON.parse(splits[1]);
	return smallestBeautifulString(s, k);
}
