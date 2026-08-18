function maxNumberOfFamilies(n: number, reservedSeats: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const reservedSeats: number[][] = JSON.parse(inputValues[1]);
	return maxNumberOfFamilies(n, reservedSeats);
}
