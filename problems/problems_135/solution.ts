function candy(ratings: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const ratings: number[] = JSON.parse(inputValues[0]);
	return candy(ratings);
}
