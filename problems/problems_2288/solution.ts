function discountPrices(sentence: string, discount: number): string {
    const d: number = (100.0 - discount) / 100.0;
	const ans: string[] = [];
	sentence.split(" ").forEach(s => {
		if (s.length > 1 && s.charAt(0) == '$') {
			let cur: number = 0
			let isNumber: boolean = true
			for (let i = 1; i < s.length; i++) {
				if (s.charAt(i) < '0' || s.charAt(i) > '9') {
					isNumber = false
					break
				}
				cur = cur * 10 + s.charCodeAt(i) - '0'.charCodeAt(0);
			}
			if (isNumber) {
				const c: number = d * cur
				ans.push(`$${c.toFixed(2)}`)
			} else {
				ans.push(s);
			}
		} else {
			ans.push(s);
		}
	})
	return ans.join(" ")
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const sentence: string = JSON.parse(splits[0]);
	const discount: number = JSON.parse(splits[1]);
	return discountPrices(sentence, discount);
}
