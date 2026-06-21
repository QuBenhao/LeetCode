function maxNumberOfBalloons(text: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const text: string = JSON.parse(inputValues[0]);
	return maxNumberOfBalloons(text);
}
