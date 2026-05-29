function getResults(queries: number[][]): boolean[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const queries: number[][] = JSON.parse(inputValues[0]);
	return getResults(queries);
}
