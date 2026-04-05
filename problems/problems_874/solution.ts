function robotSim(commands: number[], obstacles: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const commands: number[] = JSON.parse(inputValues[0]);
	const obstacles: number[][] = JSON.parse(inputValues[1]);
	return robotSim(commands, obstacles);
}
