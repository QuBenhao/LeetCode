function getRow(rowIndex: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const rowIndex: number = JSON.parse(inputValues[0]);
	return getRow(rowIndex);
}
