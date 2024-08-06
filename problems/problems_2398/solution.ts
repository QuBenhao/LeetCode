function maximumRobots(chargeTimes: number[], runningCosts: number[], budget: number): number {
	const n: number = chargeTimes.length;
	let left: number = 0, right: number = n;
	const check = (mid: number): boolean => {
		let s: number = 0;
		let q: number[] = [];
		for (let i: number = 0; i < n; i++) {
			while (q.length > 0 && chargeTimes[q[q.length - 1]] <= chargeTimes[i]) {
				q.pop();
			}
			q.push(i);
			s += runningCosts[i];
			if (i >= q[0] + mid) {
				q.shift();
			}
			if (i >= mid - 1) {
				if (s * mid + chargeTimes[q[0]] <= budget) {
					return true;
				}
				s -= runningCosts[i - mid + 1];
			}
		}
		return false;
	}
	while (left < right) {
		const mid: number = left + right + 1 >> 1;
		if (check(mid)) {
			left = mid;
		} else {
			right = mid - 1;
		}
	}
	return left;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const chargeTimes: number[] = JSON.parse(inputValues[0]);
	const runningCosts: number[] = JSON.parse(inputValues[1]);
	const budget: number = JSON.parse(inputValues[2]);
	return maximumRobots(chargeTimes, runningCosts, budget);
}
