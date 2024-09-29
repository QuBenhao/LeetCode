function timeRequiredToBuy(tickets: number[], k: number): number {
	const n: number = tickets.length;
	const ticketToBuy: number = tickets[k];
	let ans: number = 0;
	for (const [index, ticket] of tickets.entries()) {
		ans += Math.min(ticket, index > k ? ticketToBuy - 1 : ticketToBuy);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const tickets: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return timeRequiredToBuy(tickets, k);
}
