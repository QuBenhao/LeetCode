function findTheString(lcp: number[][]): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const lcp: number[][] = JSON.parse(inputValues[0]);
	return findTheString(lcp);
}
