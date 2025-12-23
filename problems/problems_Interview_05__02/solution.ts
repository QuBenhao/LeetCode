function printBin(num: number): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const num: number = JSON.parse(inputValues[0]);
	return printBin(num);
}
