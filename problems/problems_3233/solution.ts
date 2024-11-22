function nonSpecialCount(l: number, r: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const l: number = JSON.parse(inputValues[0]);
	const r: number = JSON.parse(inputValues[1]);
	return nonSpecialCount(l, r);
}
