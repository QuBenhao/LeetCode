function rotateTheBox(boxGrid: string[][]): string[][] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const boxGrid: string[][] = JSON.parse(inputValues[0]);
	return rotateTheBox(boxGrid);
}
