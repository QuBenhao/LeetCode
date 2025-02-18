function maxDistance(arrays: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const arrays: number[][] = JSON.parse(inputValues[0]);
	return maxDistance(arrays);
}
