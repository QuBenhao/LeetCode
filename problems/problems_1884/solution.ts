function twoEggDrop(n: number): number {
	return Math.floor(Math.ceil(Math.sqrt(1 + 8 * n)) / 2);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return twoEggDrop(n);
}
