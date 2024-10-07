function minimumTime(time: number[], totalTrips: number): number {
	let left = 0;
	let right = 1e18;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		let count = 0;
		for (let i = 0; i < time.length; i++) {
			count += Math.floor(mid / time[i]);
		}
		if (count >= totalTrips) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	return left;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const time: number[] = JSON.parse(inputValues[0]);
	const totalTrips: number = JSON.parse(inputValues[1]);
	return minimumTime(time, totalTrips);
}
