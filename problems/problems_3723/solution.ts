function maxSumOfSquares(num: number, sum: number): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const num: number = JSON.parse(inputValues[0]);
	const sum: number = JSON.parse(inputValues[1]);
	return maxSumOfSquares(num, sum);
}
