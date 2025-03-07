function maximumBeauty(flowers: number[], newFlowers: number, target: number, full: number, partial: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const flowers: number[] = JSON.parse(inputValues[0]);
	const newFlowers: number = JSON.parse(inputValues[1]);
	const target: number = JSON.parse(inputValues[2]);
	const full: number = JSON.parse(inputValues[3]);
	const partial: number = JSON.parse(inputValues[4]);
	return maximumBeauty(flowers, newFlowers, target, full, partial);
}
