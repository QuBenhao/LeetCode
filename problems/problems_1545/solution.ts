function findKthBit(n: number, k: number): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return findKthBit(n, k);
}
