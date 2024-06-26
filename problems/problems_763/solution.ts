function partitionLabels(s: string): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(splits[0]);
	return partitionLabels(s);
}
