function myPow(x: number, n: number): number {
	
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const x: number = JSON.parse(splits[0]);
	const n: number = JSON.parse(splits[1]);
	return myPow(x, n);
}
