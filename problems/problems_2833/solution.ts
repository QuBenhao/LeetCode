function furthestDistanceFromOrigin(moves: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const moves: string = JSON.parse(inputValues[0]);
	return furthestDistanceFromOrigin(moves);
}
