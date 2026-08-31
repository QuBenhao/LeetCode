function minMoves(classroom: string[], energy: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const classroom: string[] = JSON.parse(inputValues[0]);
	const energy: number = JSON.parse(inputValues[1]);
	return minMoves(classroom, energy);
}
