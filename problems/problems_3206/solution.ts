function numberOfAlternatingGroups(colors: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const colors: number[] = JSON.parse(inputValues[0]);
	return numberOfAlternatingGroups(colors);
}
