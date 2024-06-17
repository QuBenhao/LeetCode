function romanToInt(s: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(splits[0]);
	return romanToInt(s);
}
