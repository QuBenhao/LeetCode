function minEatingSpeed(piles: number[], h: number): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const piles: number[] = JSON.parse(inputValues[0]);
	const h: number = JSON.parse(inputValues[1]);
	return minEatingSpeed(piles, h);
}
