function countBalls(lowLimit: number, highLimit: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const lowLimit: number = JSON.parse(inputValues[0]);
	const highLimit: number = JSON.parse(inputValues[1]);
	return countBalls(lowLimit, highLimit);
}
