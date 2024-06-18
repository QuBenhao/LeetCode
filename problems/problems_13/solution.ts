function romanToInt(s: string): number {
    const romanMap = new Map<string, number>();
    romanMap.set('I', 1);
    romanMap.set('V', 5);
    romanMap.set('X', 10);
    romanMap.set('L', 50);
    romanMap.set('C', 100);
    romanMap.set('D', 500);
    romanMap.set('M', 1000);
	let ans: number = romanMap.get(s.charAt(0)) ?? 0, last: number = ans;
	for (let i: number = 1; i < s.length; i++) {
		const v: number = romanMap.get(s.charAt(i)) ?? 0;
		ans += v;
		if (last < v) {
			ans -= last << 1;
		}
		last = v;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
    const splits: string[] = inputJsonElement.split("\n");
    const s: string = JSON.parse(splits[0]);
    return romanToInt(s);
}
