function discountPrices(sentence: string, discount: number): string {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const sentence: string = JSON.parse(splits[0]);
	const discount: number = JSON.parse(splits[1]);
	return discountPrices(sentence, discount);
}
