function countPrimeSetBits(left: number, right: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const left: number = JSON.parse(inputValues[0]);
	const right: number = JSON.parse(inputValues[1]);
	return countPrimeSetBits(left, right);
}
