function distributeCandies(n: number, limit: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const limit: number = JSON.parse(inputValues[1]);
	return distributeCandies(n, limit);
}
