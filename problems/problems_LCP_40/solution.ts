function maxmiumScore(cards: number[], cnt: number): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const cards: number[] = JSON.parse(inputValues[0]);
	const cnt: number = JSON.parse(inputValues[1]);
	return maxmiumScore(cards, cnt);
}
