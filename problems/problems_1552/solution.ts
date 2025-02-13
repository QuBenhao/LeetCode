function maxDistance(position: number[], m: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const position: number[] = JSON.parse(inputValues[0]);
	const m: number = JSON.parse(inputValues[1]);
	return maxDistance(position, m);
}
