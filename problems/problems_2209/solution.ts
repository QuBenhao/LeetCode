function minimumWhiteTiles(floor: string, numCarpets: number, carpetLen: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const floor: string = JSON.parse(inputValues[0]);
	const numCarpets: number = JSON.parse(inputValues[1]);
	const carpetLen: number = JSON.parse(inputValues[2]);
	return minimumWhiteTiles(floor, numCarpets, carpetLen);
}
