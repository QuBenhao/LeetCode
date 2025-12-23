function minimumBoxes(apple: number[], capacity: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const apple: number[] = JSON.parse(inputValues[0]);
	const capacity: number[] = JSON.parse(inputValues[1]);
	return minimumBoxes(apple, capacity);
}
