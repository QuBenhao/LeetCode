function maxProfit(prices: number[]): number {
    let buy: number = -prices[0], sell: number = 0;
	for (let i: number = 1; i < prices.length; i++) {
		buy = Math.max(buy, -prices[i]);
		sell = Math.max(sell, buy + prices[i]);
	}
	return sell;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const prices: number[] = JSON.parse(inputValues[0]);
	return maxProfit(prices);
}
