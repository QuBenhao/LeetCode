function generate(numRows: number): number[][] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const numRows: number = JSON.parse(inputValues[0]);
	return generate(numRows);
}
