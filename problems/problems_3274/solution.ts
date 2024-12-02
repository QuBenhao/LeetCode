function checkTwoChessboards(coordinate1: string, coordinate2: string): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const coordinate1: string = JSON.parse(inputValues[0]);
	const coordinate2: string = JSON.parse(inputValues[1]);
	return checkTwoChessboards(coordinate1, coordinate2);
}
