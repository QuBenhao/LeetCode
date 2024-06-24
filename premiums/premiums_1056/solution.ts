function confusingNumber(n: number): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(splits[0]);
	return confusingNumber(n);
}
