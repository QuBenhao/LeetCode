function mostPoints(questions: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const questions: number[][] = JSON.parse(inputValues[0]);
	return mostPoints(questions);
}
