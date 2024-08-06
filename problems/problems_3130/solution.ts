function numberOfStableArrays(zero: number, one: number, limit: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const zero: number = JSON.parse(inputValues[0]);
	const one: number = JSON.parse(inputValues[1]);
	const limit: number = JSON.parse(inputValues[2]);
	return numberOfStableArrays(zero, one, limit);
}
