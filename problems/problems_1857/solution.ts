function largestPathValue(colors: string, edges: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const colors: string = JSON.parse(inputValues[0]);
	const edges: number[][] = JSON.parse(inputValues[1]);
	return largestPathValue(colors, edges);
}
