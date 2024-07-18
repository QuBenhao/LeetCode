function minimumLevels(possible: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const possible: number[] = JSON.parse(inputValues[0]);
	return minimumLevels(possible);
}
