function minimumTeachings(n: number, languages: number[][], friendships: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const languages: number[][] = JSON.parse(inputValues[1]);
	const friendships: number[][] = JSON.parse(inputValues[2]);
	return minimumTeachings(n, languages, friendships);
}
