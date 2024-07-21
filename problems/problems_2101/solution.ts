function maximumDetonation(bombs: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const bombs: number[][] = JSON.parse(inputValues[0]);
	return maximumDetonation(bombs);
}
