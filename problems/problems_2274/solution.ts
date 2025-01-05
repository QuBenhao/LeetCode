function maxConsecutive(bottom: number, top: number, special: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const bottom: number = JSON.parse(inputValues[0]);
	const top: number = JSON.parse(inputValues[1]);
	const special: number[] = JSON.parse(inputValues[2]);
	return maxConsecutive(bottom, top, special);
}
