function finalPositionOfSnake(n: number, commands: string[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const commands: string[] = JSON.parse(inputValues[1]);
	return finalPositionOfSnake(n, commands);
}
