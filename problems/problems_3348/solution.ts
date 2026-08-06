function smallestNumber(num: string, t: number): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const num: string = JSON.parse(inputValues[0]);
	const t: number = JSON.parse(inputValues[1]);
	return smallestNumber(num, t);
}
