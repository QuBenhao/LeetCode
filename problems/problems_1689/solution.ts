function minPartitions(n: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: string = JSON.parse(inputValues[0]);
	return minPartitions(n);
}
