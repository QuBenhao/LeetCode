function minTimeToReach(moveTime: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const moveTime: number[][] = JSON.parse(inputValues[0]);
	return minTimeToReach(moveTime);
}
