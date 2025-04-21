function idealArrays(n: number, maxValue: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const maxValue: number = JSON.parse(inputValues[1]);
	return idealArrays(n, maxValue);
}
