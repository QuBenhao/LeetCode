function pushDominoes(dominoes: string): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const dominoes: string = JSON.parse(inputValues[0]);
	return pushDominoes(dominoes);
}
