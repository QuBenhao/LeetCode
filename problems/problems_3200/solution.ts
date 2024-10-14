function maxHeightOfTriangle(red: number, blue: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const red: number = JSON.parse(inputValues[0]);
	const blue: number = JSON.parse(inputValues[1]);
	return maxHeightOfTriangle(red, blue);
}
