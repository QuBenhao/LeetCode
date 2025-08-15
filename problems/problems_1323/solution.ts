function maximum69Number (num: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const num: number = JSON.parse(inputValues[0]);
	return maximum69Number(num);
}
