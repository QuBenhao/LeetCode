function squareIsWhite(coordinates: string): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const coordinates: string = JSON.parse(inputValues[0]);
	return squareIsWhite(coordinates);
}
