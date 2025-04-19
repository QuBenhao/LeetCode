function numRabbits(answers: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const answers: number[] = JSON.parse(inputValues[0]);
	return numRabbits(answers);
}
