function closestTarget(words: string[], target: string, startIndex: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(inputValues[0]);
	const target: string = JSON.parse(inputValues[1]);
	const startIndex: number = JSON.parse(inputValues[2]);
	return closestTarget(words, target, startIndex);
}
