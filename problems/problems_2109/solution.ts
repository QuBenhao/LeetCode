function addSpaces(s: string, spaces: number[]): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const spaces: number[] = JSON.parse(inputValues[1]);
	return addSpaces(s, spaces);
}
